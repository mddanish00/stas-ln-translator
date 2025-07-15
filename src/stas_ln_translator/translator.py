import asyncio
import warnings

from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
import httpx
from tqdm.asyncio import tqdm_asyncio
from ebooklib import epub

from stas_ln_translator import config, process, connection

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)


async def translate_epub(book: epub.EpubBook) -> epub.EpubBook:
    documents = process.get_all_documents_in_epub(book)
    documents: dict[str, BeautifulSoup] = {
        id: process.preprocess_document(soup) for id, soup in documents.items()
    }

    requests: list[asyncio.Future] = []
    requests_keys: list[list[list[int]]] = []

    async with httpx.AsyncClient(timeout=None) as client:
        # Process per document
        # Divide the text lines by config.batch_size
        # Into multiple request
        for id, soup in documents.items():
            text_dict = process.extract_text_from_document(soup)
            page_keys: list[int] = []
            page_requests: list[asyncio.Future] = []
            for lines in process.chunks(text_dict, config.batch_size):
                page_requests.append(
                    connection.create_translation_request(
                        list(lines.values()),
                        client,
                        config.translator_api_url,
                        config.request_type,
                    )
                )
                page_keys.append(list(lines.keys()))
            requests.append(asyncio.gather(*page_requests))
            requests_keys.append(page_keys)

        # translated_text_docs should be a list composed of multiple list[list[str]] for a book
        # A document = list[list[str]]
        # A request = list[str]
        translated_text_docs: list[list[list[str]]] = await tqdm_asyncio.gather(
            *requests
        )

        for id, soup, translated_doc_key, translated_doc in zip(
            documents.keys(), documents.values(), requests_keys, translated_text_docs
        ):
            # Join all lists in both translated_doc_key, translated_doc
            translated_texts = [t for doc in translated_doc for t in doc]
            translated_keys = [k for doc in translated_doc_key for k in doc]
            # Join translated_keys as key, translated_doc as value
            translated_texts_dict = dict(zip(translated_keys, translated_texts))
            documents[id] = process.recombine_text_to_document(
                soup, translated_texts_dict
            )

    return documents
