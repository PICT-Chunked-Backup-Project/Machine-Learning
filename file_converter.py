import docx
import pytesseract
from PIL import Image
import aspose.words as aw
import os
import pandas as pd
import PyPDF2

class fileConverter:
    path = ""

    def __init__(self, p):
        self.path = p

    def convert_tostr(self):
        if self.path.endswith(".docx"):
            doc = docx.Document(self.path)
            fullText = []
            for para in doc.paragraphs:
                fullText.append(para.text)
                text = '\n'.join(fullText)
                print(text)
        elif self.path.endswith(".pdf"):
            pdfFileObj = open(self.path, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
            pageObj = pdfReader.getPage(0)
            text = pageObj.extract_text()
            #print(text)
        elif self.path.endswith(".csv"):
            df1 = pd.read_csv(self.path)
            text = df1.to_string()
            #print(text)
        elif self.path.endswith(".xlsx"):
            df1 = pd.read_excel(self.path)
            text = df1.to_string()
            #print(text)
        elif (self.path.endswith(".jpg") or self.path.endswith(".png") or self.path.endswith(".gif") or self.path.endswith(".jpeg") or self.path.endswith(".bmp") or self.path.endswith(".eps") or
              self.path.endswith(".raw") or
              self.path.endswith(".cr2") or self.path.endswith(".nef") or self.path.endswith(".orf") or self.path.endswith(".sr2")):

            pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
            text = pytesseract.image_to_string(Image.open(self.path))
            #print(text)
        return text
if __name__ == "__main__":
    f = fileConverter('C:\\Users\\adity\\Downloads\\itotext.png')
    f.convert_tostr()
    # convert_tostr('C:\\Backup Project\\1.pdf')
    # convert_tostr('C:\\Users\\adity\\Downloads\\itotext.png')
