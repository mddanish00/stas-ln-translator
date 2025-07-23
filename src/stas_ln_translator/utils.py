from itertools import batched
from typing import Iterator
from bs4 import BeautifulSoup
from ebooklib import epub


# Based on https://stackoverflow.com/a/77832086
# Python 3.12+
def chunks[T, R](data: dict[T, R], SIZE=10000):
    return map(dict, batched(data.items(), SIZE))


def get_EPUB_version(book: epub.EpubBook) -> int:
    """Determine the EPUB version of the book.

    Args:
        book (epub.EpubBook): EpubBook object representing the EPUB book.

    Returns:
        int: Version of EPUB. Will either return 2 or 3.
    """
    return 3 if str(book.version) == "3.0" else 2


def get_first_in_iterator[T](iterator: Iterator[T]):
    try:
        return next(iterator)
    except StopIteration:
        return None


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
            book.guide = list(set([*book.guide, *landmarks_items]))


def fix_cover_in_epub_item(book: epub.EpubBook) -> None:
    cover_guide_href: str | None = get_first_in_iterator(
        item["href"] for item in book.guide if item["type"] == "cover"
    )
    cover_image = get_first_in_iterator(
        item for item in book.get_items() if isinstance(item, epub.EpubCover)
    )

    if cover_guide_href is not None and cover_image is not None:
        cover_html: epub.EpubHtml = book.get_item_with_href(cover_guide_href)
        new_cover_html = epub.EpubCoverHtml(image_name=cover_image.file_name)
        new_cover_html.content = cover_html.content
        book.items.remove(cover_html)
        book.add_item(new_cover_html)
