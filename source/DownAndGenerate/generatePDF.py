# -*- coding: utf-8 -*-
import os
from fpdf import FPDF
import shutil
from tqdm import tqdm

def generate_pdf(path, pdf_name='output'):
  pdf = FPDF('P', 'mm', 'A4')
  jpg_files = sorted([file for file in os.listdir(path) if file.endswith('.jpg')])
  for jpg_file in tqdm(jpg_files,desc=f'Generating PDF'):
    pdf.add_page()
    page_width = 210
    page_height = 297
    x = 0
    y = 0
    pdf.image(f'{path}/{jpg_file}', x, y, page_width, page_height)
  pdf.output(f"{pdf_name}.pdf")
  tqdm.write(f"{pdf_name}.pdf generate completed!")
  shutil.rmtree(path, ignore_errors=True)