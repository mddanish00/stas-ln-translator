import sys
import importlib.metadata
import asyncclick as click


from stas_ln_translator import config


# Call back for validating file need to have '.epub' file extension
def validate_epub_file(ctx, param, value):
    if not value.endswith(".epub"):
        raise click.BadParameter(
            f"Input file {value} must have a .epub extension"
            if param.name == "input"
            else f"Output file {value} must have a .epub extension"
        )
    return value


def cleanup_temp_dir():
    if config.temp_dir is not None:
        import shutil

        shutil.rmtree(config.temp_dir)
        click.echo(f"Temporary directory '{config.temp_dir}' cleaned up")


@click.command(
    context_settings=dict(help_option_names=["-h", "--help"]),
    help="Run stas-ln-translator, an alternative standalone Light Novel translator for Sugoi Translator. Recommended usage with stas-server.",
)
@click.version_option(None, "-v", "--version", message="%(version)s")
@click.option(
    "--batch_size",
    required=False,
    default=100,
    help="Number of lines per batch in a request. Only works when request_type is 'Batch'.",
)
@click.option(
    "--request_type",
    required=False,
    default="Batch",
    help="Request type used when contacting API. Either 'Single' or 'Batch'(default).",
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
def cli(
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
        # Clean up temporary directory
        cleanup_temp_dir()
    except KeyboardInterrupt:
        click.echo("\nCtrl+C detected. Performing graceful shutdown...")
        cleanup_temp_dir()
        sys.exit(0)
