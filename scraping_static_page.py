# -*- coding: utf-8 -*-

import urllib.request
import chardet
import pandas as pd
from bs4 import BeautifulSoup
TARGET_URL = "http://konojunya.com/"
CSV_PATH = "konojunya.csv"


def scraping(url, output_name):
    # get a HTML response
    data = urllib.request.urlopen(url).read()

    # エンコーディング判別とデコード
    guess = chardet.detect(data)
    html = data.decode(guess['encoding'])

    # parse the response
    soup = BeautifulSoup(html, "lxml")

    # extract
    title = soup.find("title").text
    h1_data = soup.find("h1").text

    header = soup.find("head")
    description = header.find("meta", attrs={"name": "description"})
    description_content = description.attrs['content']

    df = pd.DataFrame({
        "title": [title],
        "h1_text": [h1_data],
        "descuription": [description_content]
    })

    df.to_csv(output_name, index=None)

if __name__ == '__main__':
    scraping(TARGET_URL, CSV_PATH)
