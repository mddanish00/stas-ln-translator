import argparse
import asyncio
import warnings
from importlib.metadata import version
from pathlib import Path

from bs4 import XMLParsedAsHTMLWarning
from ebooklib import epub

from stas_ln_translator import config, translator, utils

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)


current_version = version("stas-ln-translator")


def get_arguments() -> tuple[int, str, str, str, str, str]:
    parser = argparse.ArgumentParser(
        description="Run stas-ln-translator, an alternative standalone Light Novel translator for Sugoi Translator. Recommended usage with stas-server.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=current_version,
    )
    parser.add_argument(
        "--batch_size",
        type=int,
        default=100,
        help="Number of lines per batch in a request. Batch request type only.",
    )
    parser.add_argument(
        "--request_type",
        default="Batch",
        choices=["Single", "Batch"],
        help="Request type used when contacting API. Either 'Single' or 'Batch'.",
    )
    parser.add_argument(
        "--tag_to_translate",
        default="p,h1,h2,h3,h4,h5,h6,title",
        help="HTML elements to translate, separated by commas",
    )
    parser.add_argument(
        "--translator_api_url",
        default="http://localhost:14366",
        help="stas-server or any other Sugoi Translator compatible API URL",
    )
    parser.add_argument(
        "input",
        type=Path,
        help="Input EPUB file",
    )
    parser.add_argument(
        "output",
        type=Path,
        help="Output EPUB file",
    )

    args = parser.parse_args()

    if args.input.suffix != ".epub":
        parser.error(f"Input file {args.input} must have a .epub extension")

    if not args.input.exists():
        parser.error(f"`{args.input}` does not exist")

    if args.output.suffix != ".epub":
        parser.error(f"Output file {args.output} must have a .epub extension")

    return (
        args.batch_size,
        args.request_type,
        args.tag_to_translate,
        args.translator_api_url,
        args.input.resolve().__str__(),
        args.output.resolve().__str__(),
    )


async def cli_main():
    # Create EpubBook instance for passing to translator
    book = epub.read_epub(config.input)
    if utils.get_EPUB_version(book) == 3:
        # EBookLib don't parse EPUB landmarks, so need to add manually
        utils.add_EPUB3_landmarks_to_epub_item(book)
    utils.fix_cover_in_epub_item(book)
    toc_list = await translator.translate_toc(book)
    documents = await translator.translate_epub(book)
    utils.write_all_changes_to_epub_item(book, toc_list, documents)
    epub.write_epub(config.output, book)


def cli():
    (
        batch_size,
        request_type,
        tag_to_translate,
        translator_api_url,
        input_epub,
        output_epub,
    ) = get_arguments()
    config.loads(
        input_epub,
        output_epub,
        batch_size,
        request_type,
        tag_to_translate,
        translator_api_url,
    )
    print(f"stas-ln-translator - v{current_version}")
    config.print_config()
    asyncio.run(cli_main())
