from download import download_and_create_chapters
from scrape import get_audiobook_download_links

download_and_create_chapters(get_audiobook_download_links("https://tokybook.com/the-book-of-dust-la-belle-sauvage"))
