import sys
import asyncio
import importlib.metadata

import asyncclick as click
from ebooklib import epub

from stas_ln_translator import config, translator, process


# Call back for validating file need to have '.epub' file extension
def validate_epub_file(ctx, param, value):
    if not value.endswith(".epub"):
        raise click.BadParameter(
            f"Input file {value} must have a .epub extension"
            if param.name == "input"
            else f"Output file {value} must have a .epub extension"
        )
    return value


@click.command(
    context_settings=dict(help_option_names=["-h", "--help"], show_default=True),
    help="Run stas-ln-translator, an alternative standalone Light Novel translator for Sugoi Translator. Recommended usage with stas-server.",
)
@click.version_option(None, "-v", "--version", message="%(version)s")
@click.option(
    "--batch_size",
    required=False,
    default=100,
    help="Number of lines per batch in a request. Batch request type only.",
)
@click.option(
    "--request_type",
    required=False,
    default="Batch",
    help="Request type used when contacting API. Either 'Single' or 'Batch'.",
)
@click.option(
    "--tag_to_translate",
    required=False,
    help="HTML elements to translate, separated by commas",
    default="p,h1,h2,h3,h4,h5,h6,title",
)
@click.option(
    "--translator_api_url",
    required=False,
    help="stas-server or any other Sugoi Translator compatible API URL",
    default="http://localhost:14366",
)
@click.argument(
    "input",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, resolve_path=True),
    # help="Input EPUB file",
    callback=validate_epub_file,
)
@click.argument(
    "output",
    type=click.Path(exists=False, file_okay=True, dir_okay=False, resolve_path=True),
    # help="Output EPUB file",
    callback=validate_epub_file,
)
async def cli_main(
    input,
    output,
    translator_api_url,
    request_type,
    batch_size,
    tag_to_translate,
):
    try:
        config.loads(
            input,
            output,
            batch_size,
            request_type,
            tag_to_translate,
            translator_api_url,
        )
        click.echo(
            f"stas-ln-translator - v{importlib.metadata.version('stas-ln-translator')}"
        )
        config.print_config(click.echo)
        # Create EpubBook instance for passing to translator
        book = epub.read_epub(config.input)
        documents = await translator.translate_epub(book)
        process.write_all_documents_to_epub_item(book, documents)
        epub.write_epub(config.output, book)
    except KeyboardInterrupt:
        click.echo("Ctrl+C detected. Performing graceful shutdown...")
        sys.exit(0)


def cli():
    asyncio.run(cli_main())
