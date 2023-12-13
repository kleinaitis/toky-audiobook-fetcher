import requests


def create_audiobook_file(response, chapter_counter):
    file_name = f"Chapter{chapter_counter}.mp3"
    with open(file_name, 'wb') as output_file:
        output_file.write(response.content)


def download_audiobook_data(audiobook_links):
    # Skip the first link since it's an advertisement
    download_links = audiobook_links[1:]

    for chapter_counter, download_link in enumerate(download_links, start=1):
        response = requests.get(download_link, allow_redirects=True)
        create_audiobook_file(response, chapter_counter)

