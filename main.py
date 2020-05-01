import csv
from urllib import request


def warning(message: str):
    print(f'\033[93m{message}\033[0m')


def download_book(book_title: str, url_string: str, as_epub: bool = False):
    redirect_url = request.urlopen(url_string).geturl()

    if as_epub:
        file_name = f'{book_title}.epub'
        book_url = f'{str(redirect_url).replace("book", "download/epub")}.epub'
    else:
        file_name = f'{book_title}.pdf'
        book_url = f'{str(redirect_url).replace("book", "content/pdf")}.pdf'

    try:
        print(f'downloading: {file_name}')
        request.urlretrieve(book_url, f'./downloaded/{file_name}')
    except Exception as e:
        warning(f'failed to download {file_name}, reason: {str(e)}')


if __name__ == '__main__':
    with open('books.csv', newline='') as f:
        reader = csv.DictReader(f, fieldnames=['title', 'url'])
        for row in reader:
            title = row['title'].strip()
            url = row['url'].strip()

            download_book(title, url)
            download_book(title, url, as_epub=True)
