# -*- coding: utf-8 -*-
import requests
from fpdf import FPDF
from tqdm import tqdm
import os
import shutil

def download_image(url, filename):
    filepath = f".temp/{filename}"
    response = requests.get(url)
    with open(filepath, 'wb') as file:
        file.write(response.content)
    return filepath

def generate_pep_pdf(baseurl, start, end, pdf_filename):
    if not os.path.exists('.temp'):
        os.makedirs('.temp')
    pdf = FPDF()
    for i in tqdm(range(start, end + 1), desc="Generating PDF"):
        image_url = f"{baseurl}{i}.jpg"
        image_filename = f"{i}.jpg"
        image_filepath = download_image(image_url, image_filename)
        pdf.add_page()
        pdf.image(image_filepath, x=0, y=0, w=210, h=297)
    pdf.output(pdf_filename)
    print(f"PDF generated successfully: {pdf_filename}")
    shutil.rmtree('.temp', ignore_errors=True)

def generate_bnu_pdf(baseurl, start, end, pdf_filename, coverurl):
    if not os.path.exists('.temp'):
        os.makedirs('.temp')
    pdf = FPDF()
    coverpath=download_image(coverurl, "cover.jpg")
    pdf.add_page()
    pdf.image(coverpath, x=0, y=0, w=210, h=297)
    for i in tqdm(range(start, end + 1), desc="Generating PDF"):
        image_url = "{}{:03}.jpg".format(baseurl, i)
        image_filename = f"{i}.jpg"
        image_filepath = download_image(image_url, image_filename)
        pdf.add_page()
        pdf.image(image_filepath, x=0, y=0, w=210, h=297)
    pdf.output(pdf_filename)
    print(f"PDF generated successfully: {pdf_filename}")
    shutil.rmtree('.temp', ignore_errors=True)

if __name__ == "__main__":
    print("The part of the code is to download the book from http://www.100875.com.cn/show/resource.html and https://jc.pep.com.cn.")
    print("You can use the following functions to download the book:")
    source = input("Please input the source of the book (PEP/BNU):")
    if source == "PEP" or source == "pep":
        baseurl = input("Please input the base URL:")
        start = int(input("Please input the start page:"))
        end = int(input("Please input the end page:"))
        pdf_filename = input("Please input the PDF filename:")
        generate_pep_pdf(baseurl, start, end, pdf_filename)
    elif source == "BNU" or source == "bnu":
        baseurl = input("Please input the base URL:")
        start = int(input("Please input the start page:"))
        end = int(input("Please input the end page:"))
        pdf_filename = input("Please input the PDF filename:")
        generate_bnu_pdf(baseurl, start, end, pdf_filename)
    else:
        print("Invalid source.")