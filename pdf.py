import PyPDF2
pdfFileObject=open(r"C:\Users\dell\Desktop\backup\PdfFile.pdf",'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject) 
print("100", pdfReader.numPages)
print(pdfReader)