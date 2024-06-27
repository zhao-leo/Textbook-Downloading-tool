# -*- coding: utf-8 -*-
import json
class bookitem(object):
    BookCount = 0
    bookshelf = []
    def __init__(self,book_url=None, title=None, publisher=None, pagelist=[]):
        self.source_url = book_url
        self.title = title
        self.publisher = publisher
        self.pagelist = pagelist
        bookitem.BookCount += 1
        bookitem.bookshelf.append(self)

    def __str__(self):
        return f"Title: {self.title}\nPublisher: {self.publisher}\nTotalPages: {len(self.pagelist)}\n"

    def to_json(self, file_path):
        data = {
            "source_url": self.source_url,
            "title": self.title,
            "publisher": self.publisher,
            "pagelist": self.pagelist
        }
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def from_json(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.source_url = data['source_url']
            self.title = data['title']
            self.publisher = data['publisher']
            self.pagelist = data['pagelist']

    @classmethod
    def get_book_count(cls):
        return cls.BookCount

    @classmethod
    def to_json_list(cls, file_path):
        data = []
        for book in cls.bookshelf:
            data.append({
                "source_url": book.source_url,
                "title": book.title,
                "publisher": book.publisher,
                "pagelist": book.pagelist
            })
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @classmethod
    def from_json_list(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                bookitem(item['source_url'], item['title'], item['publisher'], item['pagelist'])


