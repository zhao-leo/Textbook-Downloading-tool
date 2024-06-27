# -*- coding: utf-8 -*-
import requests
from urllib.parse import urlparse
import re
from source.book_source.bookitem import bookitem

def get_pep_book(source_url):
    id_part = urlparse(source_url).path.split('/')[1] # get the id from the url

    searchurl=f"https://book.pep.com.cn/{id_part}/mobile/javascript/config.js"
    book_detail=requests.get(searchurl)
    book_detail=book_detail.text
    page = int(re.search(r'bookConfig\.totalPageCount=(\d+)', book_detail).group(1))
    title = re.search(r'bookConfig\.bookTitle\s*=\s*["\'](.+?)["\']', book_detail).group(1)# get the page & title from the config.js

    pagelist=[f"https://book.pep.com.cn/{id_part}/files/mobile/{i+1}.jpg" for i in range(page)]
    book = bookitem(source_url,title,"PEP",pagelist)
    return book

