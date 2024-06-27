# -*- coding: utf-8 -*-
import requests
from urllib.parse import urlparse, parse_qs
import json
from source.book_source.bookitem import bookitem

class BNUbook(bookitem):

    def __get_bnu_book_details(self):
        parsed_url = urlparse(self.__source_url)
        query_params = parse_qs(parsed_url.query)
        res_id = query_params.get('resId', [None])[0] # get the resId from the query string
        contribute_id = query_params.get('contributeId', [None])[0] # get the contributedId from the query string
        res_bookid=requests.post("http://www.100875.com.cn/ebook/catalogList",data={"resId":res_id})
        book_id=int(json.loads(res_bookid.text)['data'][0]['catalogList'][0]['bookId'])
        res_pages=requests.post("http://www.100875.com.cn/ebook/bookPictureList",data={"bookId":book_id,"contributeId":contribute_id})
        pages=int(json.loads(res_pages.text)['data'][0]['totalNum'])

        book_detail= requests.get(f"http://www.100875.com.cn/resource/querySynResourceOne?resId={res_id}")
        resdata=json.loads(book_detail.text)
        title=resdata['data']['title']
        cover=resdata['data']['coverPath']
        extracted_path = cover[:cover.rfind('/')]

        list1=[f"http://www.100875.com.cn:1315//{cover}"]
        list2=["http://www.100875.com.cn:1315//{}/{:03}.jpg".format(extracted_path,i+1) for i in range(pages)]

        self.title=title
        self.publisher="BNU"
        self.pagelist=list1+list2

    def __init__(self,book_url):
        self.__source_url=book_url
        self.__get_bnu_book_details()
