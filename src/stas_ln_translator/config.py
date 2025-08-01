# Using The Global Object Pattern described on
# https://python-patterns.guide/python/module-globals/.


from collections.abc import Callable

# How many line per batch request
batch_size = 100
# If request type is `Single`, batch_size of 1 will be enforced
# Also, post request from translation API with "translate sentence" request.
# If request type is `Batch`, post request from translation API with "translate batch" request.
request_type = "Batch"
# HTML elements to translate
tag_to_translate = ["p", "h1", "h2", "h3", "h4", "h5", "h6", "title"]
# Translator API URL
translator_api_url = "http://localhost:14366"
# Input EPUB file
input = "input.epub"
# Output EPUB file
output = "output.epub"


def loads(
    loaded_input: str,
    loaded_output: str,
    loaded_batch_size: int,
    loaded_request_type: str,
    loaded_tag_to_translate: str,
    loaded_translator_api_url: str,
):
    global input, output, batch_size, request_type, tag_to_translate, translator_api_url

    if loaded_batch_size < 1:
        loaded_batch_size = 1

    if loaded_request_type not in ["Single", "Batch"]:
        loaded_request_type = "Batch"

    if loaded_request_type == "Single":
        loaded_batch_size = 1

    input = loaded_input
    output = loaded_output
    batch_size = loaded_batch_size
    request_type = loaded_request_type
    tag_to_translate = loaded_tag_to_translate.split(",")
    translator_api_url = loaded_translator_api_url


# Print current config values
# Can replace print function
# By default, use normal print function, can be changed to click.echo
def print_config(print_func: Callable[[str], None] = print):
    print_func("-------------------------------------------------------")
    print_func("Current configuration:")
    print_func(f"-- Input EPUB file: {input}")
    print_func(f"-- Output EPUB file: {output}")
    print_func(f"-- Batch size: {batch_size}")
    print_func(f"-- Request type: {request_type}")
    print_func(f"-- HTML elements to translate: {tag_to_translate}")
    print_func(f"-- Translator API URL: {translator_api_url}")
    print_func("-------------------------------------------------------")
