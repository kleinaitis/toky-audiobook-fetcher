import requests
from bs4 import BeautifulSoup
from urllib.parse import quote, urljoin
import re

links_array = []


def get_audiobook_download_links(URL):
    global links_array
    URL = URL
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    script_tags = soup.find_all("script")

    # Tokybook stores the "tracks" object in the 19th script tag on every audiobook page
    target_index = 18

    if 0 <= target_index < len(script_tags):
        script_content = script_tags[target_index].string
        pattern = re.compile(r'"chapter_link_dropbox"\s*:\s*"(.*?)",')

        matches = re.findall(pattern, script_content)

        for match in matches:
            # Replaces spaces with %20 in the filename
            formatted_link = quote(match, safe='/:')

            # Replace %5C with / in the filename
            formatted_link = formatted_link.replace('%5C', '/')

            full_link = urljoin("https://files02.tokybook.com/audio/", formatted_link)

            links_array.append(f"{full_link}")

    else:
        print(f"Script tag at index {target_index} not found.")

    return links_array