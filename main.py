from download import download_audiobook_data
from scrape import get_audiobook_download_links

audiobook_links = get_audiobook_download_links("")
download_audiobook_data(audiobook_links)
