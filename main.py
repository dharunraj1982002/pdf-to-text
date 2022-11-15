from pytesseract import pytesseract
from pdf2image import convert_from_path
import glob

path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd = path_to_tesseract
pdfs = glob.glob("goa3.pdf")

for pdf_path in pdfs:
    pages = convert_from_path(pdf_path, 500,poppler_path=r'C:\Program Files\poppler-0.68.0_x86\bin')

    for pageNum,imgBlob in enumerate(pages):
        text = pytesseract.image_to_string(imgBlob,lang='eng')

        with open(f'{pdf_path[:-4]}_page{pageNum}.txt', 'w') as the_file:
            the_file.write(text)