# -*- coding: utf-8 -*-
#当前文件路径 ../book_source/pep.py
import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys
# para_download 文件路径 ../downloader/para_download.py
sys.path.append(f"{os.getcwd()}\downloader")
import para_download

def get_pep_book_details(book_url):
    response = requests.get(book_url)
    response.encoding = 'utf-8'  # 设置响应的编码为UTF-8，根据实际情况选择合适的编码
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find('title')
    print(f"Book Name: {title.text}")

    parsed_url = urlparse(book_url)
    path = parsed_url.path
    id_part = path.split('/')[1]
    return title.text, id_part

def pep_main():
    BOOK_URL = input("Please input the book URL:")
    START_PAGE = int(input("Please input the start page:"))
    END_PAGE = int(input("Please input the end page:"))

    BOOK_NAME,BOOK_ID = get_pep_book_details(BOOK_URL)

    baseurl = f"https://book.pep.com.cn/{BOOK_ID}/files/mobile/"

    try:
        para_download.generate_pep_pdf(baseurl, START_PAGE, END_PAGE, f"{BOOK_NAME}.pdf")
    except Exception as e:
        print(f"Error: {e}")
    os.system("pause")

if __name__ == "__main__":
    print("Hte part of the code is to download the book from https://jc.pep.com.cn/.")
    print("What you need to do is to EXPOLRE https://jc.pep.com.cn/")
    print("CHOOSE a textbook, COPY its URL and set START and END page")
    while True:
        pep_main()
        print("Do you want to download another book?")
        choice = input("Please input Y/N:")
        if choice.upper() != "Y":
            break