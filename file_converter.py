import docx
import pytesseract
from PIL import Image
import aspose.words as aw
import os
import pandas as pd
import PyPDF2


# def convert_text1():
# text1 = textract.process(  # filepath of the file to be converted)
# text2=text1.decode()
# text_file=open(  # file path on which you want to write the text)
# text_file.write(text2)
# text_file.close()


def convert_tostr(in_file):
    if in_file.endswith(".docx"):
        doc = docx.Document(in_file)
        fullText = []
        for para in doc.paragraphs:
          fullText.append(para.text)
          text='\n'.join(fullText)
          print(text)
    elif in_file.endswith(".pdf"):
        pdfFileObj = open(in_file, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj,strict=False)
        pageObj = pdfReader.getPage(0)
        text=pageObj.extract_text()
        print(text)  
    elif in_file.endswith(".csv"):
        df1 = pd.read_csv(in_file)
        text=df1.to_string()
        print(text)
    elif in_file.endswith(".xlsx"):
        df1 = pd.read_excel(in_file)
        text=df1.to_string()
        print(text)
    elif (in_file.endswith(".jpg") or in_file.endswith(".png") or in_file.endswith(".gif") or in_file.endswith(".jpeg") or in_file.endswith(".bmp") or in_file.endswith(".eps") or
    in_file.endswith(".raw") or
    in_file.endswith(".cr2") or in_file.endswith(".nef") or in_file.endswith(".orf") or in_file.endswith(".sr2")):
    
      pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

      text = pytesseract.image_to_string(Image.open(in_file))
      print(text)


convert_tostr('C:\\Backup Project\\1.pdf')
convert_tostr('C:\\Users\\adity\\Downloads\\itotext.png')
