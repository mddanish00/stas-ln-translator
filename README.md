# stas-ln-translator

An alternative standalone Light Novel translator for Sugoi Translator.

<div align="center">

 ![GitHub License](https://img.shields.io/github/license/mddanish00/stas-ln-translator?style=flat-square) ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/mddanish00/stas-ln-translator/release-please.yml?style=flat-square) [![Buy Me A Coffee](https://img.shields.io/badge/mddanish00-black?style=flat-square&logo=buymeacoffee&logoColor=black&label=Buy%20Me%20A%20Coffee&labelColor=%23FFDD00)](https://www.buymeacoffee.com/mddanish00) [![Ko-fi](https://img.shields.io/badge/mddanish00-%2372A4F2?style=flat-square&logo=kofi&label=Ko-fi&labelColor=%23F4EFE7)](https://ko-fi.com/mddanish00)

</div>

stas-ln-translator name is an abbreviation of Sugoi Translator Alternative Standalone Light Novel Translator.

Some parts of this program are based on Light-Novel-EPUB-Translator, which is included in Sugoi Translator.

Not affiliated with Sugoi Translator.

## Features

- Fast because API requests to the Server are handled concurrently.
- Batch mode is used by default to cut down the number of requests needed significantly.
- [stas-server](https://github.com/mddanish00/stas-server) as a first-class citizen with compatibility with Sugoi Translator.
- Standalone, not tightly coupled like Light-Novel-EPUB-Translator.

## User Guide

### Requirements

- [stas-server](https://github.com/mddanish00/stas-server) or Sugoi Offline Translator (only `request_type=Single` can be used).

- Python 3.12 or Python 3.13. Python 3.14 and later are not yet supported.

### Installation

This project is not intended as a library, so installation through `uv` is recommended.

It is recommended to use [my Python Package Index](https://mddanish00.github.io/python-index/simple) for as shown as below to install this package.

You can also directly download the wheel in the [Releases](https://github.com/mddanish00/stas-ln-translator/releases) and install the package.

```commandline
uv tool install stas-ln-translator --index https://mddanish00.github.io/python-index/simple
```

### Upgrade

```commandline
uv tool upgrade stas-ln-translator
```

### Running Program

```commandline
Usage: stas-ln-translator [OPTIONS] INPUT OUTPUT

  Run stas-ln-translator, an alternative standalone Light Novel translator for
  Sugoi Translator. Recommended usage with stas-server.

Options:
  -v, --version              Show the version and exit.
  --batch_size INTEGER       Number of lines per batch in a request. Batch
                             request type only.  [default: 100]
  --request_type TEXT        Request type used when contacting API. Either
                             'Single' or 'Batch'.  [default: Batch]
  --tag_to_translate TEXT    HTML elements to translate, separated by commas
                             [default: p,h1,h2,h3,h4,h5,h6,title]
  --translator_api_url TEXT  stas-server or any other Sugoi Translator
                             compatible API URL  [default:
                             http://localhost:14366]
  -h, --help                 Show this message and exit.
```

#### Options

|Name|Default|Description|
|----|-------|-----------|
|batch_size|100|Number of lines per batch in a request.|
|request_type|Batch|Request type used when contacting the API. Either `Single` or `Batch`.|
|tag_to_translate|p,h1,h2,h3,h4,h5,h6,title|HTML elements to translate, separated by commas.|
|translator_api_url|http://localhost:14366|[stas-server](https://github.com/mddanish00/stas-server) or any other Sugoi Translator compatible API URL.|

## Development

This project is developed using the latest Python and managed by uv.

To start developing for this project, make sure to install uv. It will automatically download uv-managed Python if your system Python is not 3.13. It will not clash with your system Python because it is only used for this project.

Refer to [uv official docs](https://docs.astral.sh/uv/getting-started/installation/) for the installation instructions.

Initialise the virtual environment and install dependencies.

```commandline
uv sync
```

Launch and test the server.

```commandline
uv run stas-ln-translator
```

Build the project wheel.

```commandline
uv build --wheel
```

## Like this project?

Star this project if it is useful for you.

Also, consider buying me a coffee!

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/mddanish00)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/yellow_img.png)](https://www.buymeacoffee.com/mddanish00)

## License

This project is licensed under the [MIT license](./LICENSE).

## Other License

Light-Novel-EPUB-Translator project is part of the Sugoi Japanese Toolkit and is licensed under the [MIT license](./LICENSE-Light-Novel-EPUB-Translator).

## Acknowledgement

- Thanks to [MingShiba](https://www.patreon.com/mingshiba) for creating the Sugoi Japanese Toolkit and making high-quality (still machine translation) available to enjoy many untranslated Japanese works.
