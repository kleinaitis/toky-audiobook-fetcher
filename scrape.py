import requests
from bs4 import BeautifulSoup
from urllib.parse import quote, urljoin
import re


def get_audiobook_title(url):
    return url.rsplit("/", 1)[1].replace('-', ' ').title()


def fetch_audiobook_script_content(audiobook_url):
    # Tokybook stores the "tracks" object in the 19th script tag on every audiobook page
    target_script_index = 18
    try:
        page = requests.get(audiobook_url)
        soup = BeautifulSoup(page.content, "html.parser")
        script_tags = soup.find_all("script")

        if 0 <= target_script_index < len(script_tags):
            script_content = script_tags[target_script_index].string
            return script_content
    except requests.RequestException as e:
        print(f"Error fetching audiobook script content: {e}")
        return None


def extract_and_format_download_links(audiobook_url):
    script_content = fetch_audiobook_script_content(audiobook_url)

    if script_content:
        link_pattern = re.compile(r'"chapter_link_dropbox"\s*:\s*"(.*?)",')
        download_links = []

        matches = re.findall(link_pattern, script_content)

        for match in matches:
            # Replaces spaces with %20 in the filename
            formatted_link = quote(match, safe='/:')

            # Replace %5C with / in the filename
            formatted_link = formatted_link.replace('%5C', '/')

            full_link = urljoin("https://files02.tokybook.com/audio/", formatted_link)

            download_links.append(f"{full_link}")
        return download_links
    else:
        return []
