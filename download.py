import requests


def download_and_create_chapters(url_list):
    chapter_counter = 1

    # Skip the first link since it's an advertisement
    download_links = url_list[1:]

    for download_link in download_links:
        file_name = f"Chapter{chapter_counter}.mp3"
        audiobook_data = requests.get(download_link, allow_redirects=True)

        with open(file_name, 'wb') as output_file:
            output_file.write(audiobook_data.content)
            chapter_counter += 1
