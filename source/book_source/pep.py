# -*- coding: utf-8 -*-
import requests
from urllib.parse import urlparse
import re
from source.book_source.bookitem import bookitem

class PEPbook(bookitem):

    def __get_pep_book_details(self):
        id_part = urlparse(self.__source_url).path.split('/')[1] # get the id from the url

        searchurl=f"https://book.pep.com.cn/{id_part}/mobile/javascript/config.js"
        book_detail=requests.get(searchurl)
        book_detail=book_detail.text
        page = int(re.search(r'bookConfig\.totalPageCount=(\d+)', book_detail).group(1))
        title = re.search(r'bookConfig\.bookTitle\s*=\s*["\'](.+?)["\']', book_detail).group(1)# get the page & title from the config.js

        self.title=title
        self.publisher="PEP"
        self.pagelist=[f"https://book.pep.com.cn/{id_part}/files/mobile/{i+1}.jpg" for i in range(page)]

    def __init__(self,book_url):
        self.__source_url=book_url
        self.__get_pep_book_details()