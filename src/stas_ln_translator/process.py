from itertools import batched
from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup

from stas_ln_translator import config


def get_all_documents_in_epub(book: epub.EpubBook) -> dict[str, BeautifulSoup]:
    """Retrieve all documents from an EPUB book and return them as a dictionary.

    Args:
        book (epub.EpubBook): EpubBook object representing the EPUB book.

    Returns:
        dict[str, BeautifulSoup]: Dictionary with document IDs as keys and BeautifulSoup objects as values.
    """
    return {
        item.id: BeautifulSoup(item.content, "lxml")
        for item in book.get_items_of_type(ITEM_DOCUMENT)
        if item.is_chapter()
    }


def write_all_documents_to_epub_item(
    book: epub.EpubBook, documents: dict[str, BeautifulSoup]
) -> None:
    """Write all documents back to the EpubBook item.

    Args:
        book (epub.EpubBook): EpubBook object representing the EPUB book.
        documents (dict[str, BeautifulSoup]): Dictionary with document IDs as keys and BeautifulSoup objects as values.
    """
    for item in book.get_items_of_type(ITEM_DOCUMENT):
        currentSoup = documents[item.id]
        item.content = str(currentSoup.prettify())
        # Only body will preserved by EBookLib, so we need to manually add title tag back.
        if currentSoup.title is not None and currentSoup.title.string is not None:
            item.title = currentSoup.title.string


def preprocess_document(soup: BeautifulSoup) -> BeautifulSoup:
    """Preprocess the document to remove specific tags and clean up the structure.

    Args:
        soup (BeautifulSoup): BeautifulSoup object containing the document to be processed.

    Returns:
        BeautifulSoup: Processed BeautifulSoup object with specific tags removed or cleaned.
    """
    # Remove all <rt> tags to eliminate furigana
    for rt in soup.find_all("rt"):
        rt.decompose()

    # Remove all <rb> tags
    for rb in soup.find_all("rb"):
        rb.decompose()

    # Remove <ruby> tags and preserve their content
    for ruby in soup.find_all("ruby"):
        ruby_contents = [child for child in ruby.contents if not child.name == "rt"]
        for content in ruby_contents:
            ruby.insert_before(content)  # Insert <ruby> content before the tag
        ruby.decompose()  # Remove the <ruby> tag itself

    # Find all <p> tags
    for p_tag in soup.find_all("p"):
        # Remove <span> tags but preserve their content
        for span in p_tag.find_all("span"):
            span.unwrap()

        # Remove <a> tags but preserve their content
        for a in p_tag.find_all("a"):
            a.unwrap()

        # Remove newline in p content
        p_tag.string = "".join(p_tag.stripped_strings)

    return soup


def extract_text_from_document(soup: BeautifulSoup) -> dict[int, str]:
    """Extract text from the document and return it as a dictionary.

    Args:
        soup (BeautifulSoup): BeautifulSoup object containing the document to extract text from.


    Returns:
        dict[int, str]: Dictionary with indices as keys and text content as values.
    """
    return {
        index: tag.get_text(strip=True)
        for index, tag in enumerate(
            soup.find_all(lambda t: t.name in config.tag_to_translate)
        )
    }


def recombine_text_to_document(
    soup: BeautifulSoup, translated_texts: dict[int, str]
) -> BeautifulSoup:
    """Recombine translated texts back into the document.

    Args:
        soup (BeautifulSoup): BeautifulSoup object containing the document.
        translated_texts (dict[int, str]): Dictionary with indices as keys and translated text as values.

    Returns:
        BeautifulSoup: Recombined BeautifulSoup object with translated texts inserted back into the document.
    """
    for index, tag in enumerate(
        soup.find_all(lambda t: t.name in config.tag_to_translate)
    ):
        # Assume soup.find_all and translated_texts dict result in same list length
        tag.string = translated_texts[index]
    return soup


# Based on https://stackoverflow.com/a/77832086
# Python 3.12+
def chunks(data: dict, SIZE=10000):
    return map(dict, batched(data.items(), SIZE))
