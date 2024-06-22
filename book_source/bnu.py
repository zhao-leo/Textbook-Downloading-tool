# -*- coding: utf-8 -*-
#当前文件路径 ../book_source/bnu.py
import requests
import os
from urllib.parse import urlparse, parse_qs
import sys
import json
# para_download 文件路径 ../downloader/para_download.py
sys.path.append(f"{os.getcwd()}\downloader")
import para_download

def get_bnu_book_details(book_url):
    parsed_url = urlparse(book_url)
    query_params = parse_qs(parsed_url.query)
    res_id = query_params.get('resId', [None])[0]
    search_url=f"http://www.100875.com.cn/resource/querySynResourceOne?resId={res_id}"
    book_detail= requests.get(search_url)
    resdata=json.loads(book_detail.text)
    title=resdata['data']['title']
    url=resdata['data']['coverPath']
    extracted_path = url[:url.rfind('/')]

    print(extracted_path)
    print(f"Book Name: {title}")
    return title, extracted_path, url

def bnu_main():
    BOOK_URL = input("Please input the book URL:")
    START_PAGE = int(input("Please input the start page:"))
    END_PAGE = int(input("Please input the end page:"))

    BOOK_NAME,BOOK_ID,COVER = get_bnu_book_details(BOOK_URL)

    baseurl = f"http://www.100875.com.cn:1315//{BOOK_ID}"
    coverurl= f"http://www.100875.com.cn:1315//{COVER}"
    try:
        para_download.generate_bnu_pdf(baseurl, START_PAGE, END_PAGE-1, f"{BOOK_NAME}.pdf", coverurl)
    except Exception as e:
        print(f"Error: {e}")
    os.system("pause")

if __name__ == "__main__":
    print("Hte part of the code is to download the book from http://www.100875.com.cn/.")
    print("What you need to do is to EXPOLRE http://www.100875.com.cn/show/resource.html")
    print("CHOOSE a textbook, COPY its URL and set START and END page")
    while True:
        bnu_main()
        print("Do you want to download another book?")
        choice = input("Please input Y/N:")
        if choice.upper() != "Y":
            break