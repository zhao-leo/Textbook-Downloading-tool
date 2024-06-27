# -*- coding: utf-8 -*-
class bookitem(object):
    def __init__(self,book_url, title=None, publisher=None, pagelist=[],):
        self.__source_url = book_url
        self.title = title
        self.publisher = publisher
        self.pagelist = pagelist
    def __str__(self):
        return f"Title: {self.title}\nPublisher: {self.publisher}\nTotalPages: {len(self.pagelist)}\n"

