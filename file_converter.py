import docx
import pytesseract
from PIL import Image
import aspose.words as aw
import os
import pandas as pd
import PyPDF2



class fileConverter:
    path = ""
    tesseractFilePath=""

    def __init__(self, p,t):
        self.path = p
        self.tesseractFilePath=t

    def convert_tostr(self):
        imgSuffixes = (".jpg", ".png", ".gif", ".jpeg", ".raw", ".cr2", ".nef", ".orf", ".sr2")
        if self.path.endswith(".docx"):
            doc = docx.Document(self.path)
            fullText = []
            for para in doc.paragraphs:
                fullText.append(para.text)
                text = '\n'.join(fullText)
                print(text)
        elif self.path.endswith(".txt"):
            with open(self.path,encoding='utf-8') as f:
                text=f.readlines()
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

        elif self.path.endswith(imgSuffixes):

            pytesseract.pytesseract.tesseract_cmd = self.tesseractFilePath
            text = pytesseract.image_to_string(Image.open(self.path))
            #print(text)
        return text
# if __name__ == "__main__":
#     f = fileConverter('C:\\Users\\adity\\Downloads\\itotext.png')
#     f.convert_tostr()
#     # convert_tostr('C:\\Backup Project\\1.pdf')
#     # convert_tostr('C:\\Users\\adity\\Downloads\\itotext.png')
