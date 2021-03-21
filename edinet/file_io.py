import datetime, os, requests
from bs4 import BeautifulSoup

from setting import OUTPUT_DIR

def save_document(response: requests.models.Response, doc_control_num: str, date: datetime.date, doc_type: str):
    str_date = date.strftime("%Y-%m-%d")
    filepath = os.path.join(OUTPUT_DIR, str_date, doc_type, f"{doc_control_num}.zip")
    with open(filepath, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)

def load_html_soup_format(path: str) -> BeautifulSoup:
    with open(path, encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'lxml')
    return soup