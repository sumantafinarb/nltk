import PyPDF2

myFile = open('workingwithpdf/US_Declaration.pdf',mode='rb') # reading in binary method

pdfReader = PyPDF2.PdfFileReader(myFile)
pdfReader.numPages

pageOne = pdfReader.getPage(0)

pageOne.extractText()


adiPdf = open('workingwithpdf/amazon.pdf',mode='rb')

adiPdfReader = PyPDF2.PdfFileReader(adiPdf)

adiPdfReader.numPages

adiPdfReader.getPage(16).extractText()