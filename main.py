# -*- coding: utf-8 -*-
import requests
from fpdf import FPDF
from tqdm import tqdm
import shutil
import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import time

def get_para(book_url):
    response = requests.get(book_url)
    time.sleep(1)
    response.encoding = 'utf-8'  # 设置响应的编码为UTF-8，根据实际情况选择合适的编码
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find('title')
    print(f"Book Name: {title.text}")

    parsed_url = urlparse(book_url)
    path = parsed_url.path
    id_part = path.split('/')[1]
    print(f"Book Id:{id_part}")
    return title.text, id_part

def download_image(url, filename):
    filepath = f".src/{filename}"
    response = requests.get(url)
    with open(filepath, 'wb') as file:
        file.write(response.content)
    return filepath

def generate_pdf(baseurl, start, end, pdf_filename):
    if not os.path.exists('.src'):
        os.makedirs('.src')
    pdf = FPDF()
    for i in tqdm(range(start, end + 1), desc="Generating PDF"):
        image_url = f"{baseurl}{i}.jpg"
        image_filename = f"{i}.jpg"
        image_filepath = download_image(image_url, image_filename)
        pdf.add_page()
        pdf.image(image_filepath, x=0, y=0, w=210, h=297)
    pdf.output(pdf_filename)

def main():
    BOOK_URL = input("Please input the book URL:")
    START_PAGE = int(input("Please input the start page:"))
    END_PAGE = int(input("Please input the end page:"))

    BOOK_NAME,BOOK_ID = get_para(BOOK_URL)

    baseurl = f"https://book.pep.com.cn/{BOOK_ID}/files/mobile/"

    try:
        generate_pdf(baseurl, START_PAGE, END_PAGE, f"{BOOK_NAME}.pdf")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"PDF generated successfully: {BOOK_NAME}.pdf")
        shutil.rmtree('.src', ignore_errors=True)
    os.system("pause")
if __name__ == "__main__":
    i=1
    print("Welcome To Use The PEP Textbook Downloading Tool")
    print("What you need to do is to EXPOLRE https://jc.pep.com.cn/")
    print("CHOOSE a textbook, COPY its URL and set START and END page")
    while(i):
        switch = input("Do you want to download a textbook? (Y/N)")
        if switch == "Y" or switch == "y":
            main()
        else:
            i=0
            print("Thank you for using the PEP Textbook Downloading Tool")
            os.system("pause")