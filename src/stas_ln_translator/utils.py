from collections.abc import Iterable, Iterator
from itertools import batched

from bs4 import BeautifulSoup
from ebooklib import epub, ITEM_DOCUMENT

type TOCList = list[epub.Link | tuple[epub.Section, TOCList]]


# Based on https://stackoverflow.com/a/77832086
# Python 3.12+
def chunks(data: Iterable, size=10000):
    return map(
        data.__class__, batched(data.items() if hasattr(data, "items") else data, size)
    )


def get_EPUB_version(book: epub.EpubBook) -> int:
    """Determine the EPUB version of the book.

    Args:
        book (epub.EpubBook): EpubBook object representing the EPUB book.

    Returns:
        int: Version of EPUB. Will either return 2 or 3.
    """
    return 3 if str(book.version).startswith("3") else 2


def get_first_in_iterator[T](iterator: Iterator[T]):
    return next(iterator, None)


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


def write_all_changes_to_epub_item(
    book: epub.EpubBook, toc_list: TOCList, documents: dict[str, BeautifulSoup]
) -> None:
    """Write all documents back to the EpubBook item.

    Args:
        book (epub.EpubBook): EpubBook object representing the EPUB book.
        documents (dict[str, BeautifulSoup]): Dictionary with document IDs as keys and BeautifulSoup objects as values.
    """
    book.toc = toc_list
    for item in book.get_items_of_type(ITEM_DOCUMENT):
        if not item.is_chapter():
            continue
        currentSoup = documents[item.id]
        item.content = str(currentSoup.prettify())
        # Only body will preserved by EBookLib, so we need to manually add title tag back.
        if currentSoup.title is not None and currentSoup.title.string is not None:
            item.title = currentSoup.title.string


def add_EPUB3_landmarks_to_epub_item(book: epub.EpubBook) -> None:
    """Get EPUB3 landmarks from the EPUB and add them to the EpubBook guide list.

    Args:
        book (epub.EpubBook): EpubBook object representing the EPUB book.
    """
    # If the EPUB book actually follow standard, this will definitely not None
    nav_item = get_first_in_iterator(
        item for item in book.get_items() if isinstance(item, epub.EpubNav)
    )

    if nav_item is not None:
        soup = BeautifulSoup(nav_item.content, "lxml")
        nav_landmarks = soup.find("nav", attrs={"epub:type": "landmarks"})

        if nav_landmarks is not None:
            landmarks_items = [
                {"href": t["href"], "title": t.string, "type": t["epub:type"]}
                for t in nav_landmarks.find_all("a")
            ]
            # Make sure no duplicate
            existing_hrefs = {item["href"] for item in book.guide}
            for landmark in landmarks_items:
                if (
                    landmark["href"] not in existing_hrefs
                    and f"Text/{landmark['href']}" not in existing_hrefs
                ):
                    book.guide.append(landmark)


def fix_cover_in_epub_item(book: epub.EpubBook) -> None:
    cover_guide_href: str | None = get_first_in_iterator(
        item["href"] for item in book.guide if item["type"] == "cover"
    )
    cover_image = get_first_in_iterator(
        item for item in book.get_items() if isinstance(item, epub.EpubCover)
    )

    if cover_guide_href is not None and cover_image is not None:
        cover_html: epub.EpubHtml | None = book.get_item_with_href(cover_guide_href)
        if cover_html is not None:
            new_cover_html = epub.EpubCoverHtml(
                uid=cover_html.id,
                file_name=cover_html.file_name,
                image_name=f"../{cover_image.file_name}",
            )
            new_cover_html.content = cover_html.content
            new_cover_html.is_linear = cover_html.is_linear
            book.items.remove(cover_html)
            book.add_item(new_cover_html)


def flatten_toc_list(
    toc_list: TOCList, index_prefix: str | None = None
) -> tuple[list[epub.Link | epub.Section], list[str]]:
    """Flatten the table of contents (TOC) list into a flat list of EpubLink and EpubSection objects, along with their hierarchical indices.

    Args:
        toc_list (TOCList): The table of contents (TOC) list to be flattened.
        index_prefix (str | None, optional): The prefix for the hierarchical index. Defaults to None.

    Returns:
        tuple[list[epub.Link | epub.Section], list[str]]: A tuple containing two lists: the first list contains flattened EpubLink and EpubSection objects, and the second list contains their corresponding hierarchical indices.
    """
    flattened_list: list[epub.Link | epub.Section] = []
    index_list: list[str] = []

    for i, item in enumerate(toc_list):
        current_index = f"{index_prefix}-{i}" if index_prefix else str(i)
        if isinstance(item, epub.Link):
            flattened_list.append(item)
            index_list.append(current_index)
        elif isinstance(item, tuple) and isinstance(item[0], epub.Section):
            flattened_list.append(item[0])
            index_list.append(current_index)
            nested_flattened, nested_index = flatten_toc_list(item[1], current_index)
            flattened_list.extend(nested_flattened)
            index_list.extend(nested_index)
    return flattened_list, index_list


def restore_toc_list(
    flattened_list: list[epub.Link | epub.Section], index_list: list[str]
) -> TOCList:
    """Restore the table of contents (TOC) list from a flattened list of EpubLink and EpubSection objects and their hierarchical indices.

    Args:
        flattened_list (list[epub.Link  |  epub.Section]): The flattened list of EpubLink and EpubSection objects.
        index_list (list[str]): The hierarchical indices corresponding to the flattened list.

    Returns:
        TOCList: The restored table of contents (TOC) list.
    """
    assert len(flattened_list) == len(index_list)

    items_by_index = dict(zip(index_list, flattened_list))
    children_by_parent_index: dict[str, list[str]] = {}

    for index in index_list:
        parent_index = "root"
        if "-" in index:
            parent_index = index.rpartition("-")[0]

        children_by_parent_index.setdefault(parent_index, []).append(index)

    def build_tree(parent_index: str) -> TOCList:
        restored_list: TOCList = []
        child_indices = children_by_parent_index.get(parent_index, [])

        for child_index in child_indices:
            item = items_by_index[child_index]
            if isinstance(item, epub.Link):
                restored_list.append(item)
            elif isinstance(item, epub.Section):
                restored_list.append((item, build_tree(child_index)))
        return restored_list

    return build_tree("root")
