# stas-ln-translator

An alternative standalone Light Novel translator for Sugoi Translator.

stas-ln-translator name is an abbreviation of Sugoi Translator Alternative Standalone Light Novel Translator.

Some parts of this program based on Light-Novel-EPUB-Translator that included in Sugoi Translator.

Not affiliated with Sugoi Translator.

## Features

- Fast because API requests to Server are handled concurrently.
- Batch mode by default to cut down number of requests needed significantly.
- stas-server as a first-class citizen with compatibility with Sugoi Translator.
- Standalone, not tightly coupled like Light-Novel-EPUB-Translator.

## User Guide

### Requirements

- stas-server or Sugoi Offline Translator (only `request_type=Single` can be used).

- Python 3.12 or Python 3.13. Python 3.14 and above are still not supported.

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
  --batch_size INTEGER       Number of lines per batch in a request. Only
                             works when request_type is 'Batch'.
  --request_type TEXT        Request type used when contacting API. Either
                             'Single' or 'Batch'(default).
  --tag_to_translate TEXT    HTML elements to translate, separated by commas
  --translator_api_url TEXT  stas-server or any other Sugoi Translator
                             compatible API URL
  -h, --help                 Show this message and exit.
```

#### Options

|Name|Default|Description|
|----|-------|-----------|
|batch_size|100|Number of lines per batch in a request.|
|request_type|Batch|Request type used when contacting API. Either `Single` or `Batch`.|
|tag_to_translate|p,h1,h2,h3,h4,h5,h6,title|HTML elements to translate, separated by commas.|
|translator_api_url|http://localhost:14366|stas-server or any other Sugoi Translator compatible API URL.|

## Development

This project is developed using the latest Python and managed by uv.

To start developing for this project, make sure to install uv. It will automatically download uv-managed Python if your system Python is not 3.13. It will not clash with your system Python because it is only used for this project.

Refer to [uv official docs](https://docs.astral.sh/uv/getting-started/installation/) for the installation instructions.

You need to make sure install ICU if in Linux yourself. For Windows, you need to use my python index to install PyICU.

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

## License

This project is licensed under the [MIT license](./LICENSE).

## Other License

Light-Novel-EPUB-Translator project is part of Sugoi Japanese Toolkit is licensed under the [MIT license](./LICENSE-Light-Novel-EPUB-Translator).

## Acknowledgement

- Thanks to [MingShiba](https://www.patreon.com/mingshiba) for creating the Sugoi Japanese Toolkit and making high-quality (still machine translation) available to enjoy many untranslated Japanese works.