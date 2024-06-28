# -*-encoding:utf-8-*-
from source.book_source import pep, bnu
from source.book_source.bookitem import bookitem
book1 = pep.get_pep_book("https://book.pep.com.cn/1284001101161/mobile/index.html")
book2 = bnu.get_bnu_book("hhttp://www.100875.com.cn/show/resourceDetail_eBookAndTeacher.html?resId=b8ea42ad177f4396872d7fc53911d7d5&type=SYN&contributeId=9292&tp=Ebook")

book1.to_json('book1.json')
