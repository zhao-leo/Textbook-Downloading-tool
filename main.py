# -*- coding: utf-8 -*-
from source.book_source import bnu
from source.DownAndGenerate.downloader import downloader
from source.DownAndGenerate.generatePDF import generate_pdf

def main():
    PATH="./temp"
    book_url = input("Waiting for the commad(URL to download OR 0 to exit):")
    if book_url == "0":
        print('Bye!')
        exit(0)

    elif "100875.com.cn" in book_url:
        book = bnu.get_bnu_book(book_url)
        book_download = downloader(book.pagelist, PATH)
        book_download.start()
        book_download.join()
        generate_pdf(PATH, book.title)

print("Welcome to the textbook downloader!")
print("Now support the following sources:")
print("1. BNU ( http://www.100875.com.cn/show/resource.html )")
print("Press 0 to Exit the program.")
print("Please input the URL and we will auto download the book for you.")
while True:
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")