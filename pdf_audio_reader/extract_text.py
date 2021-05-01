import PyPDF2

file_object = open("abc.pdf", "rb")

pdfFileReader = PyPDF2.PdfFileReader(file_object)

extract_text = ""

for pageNum in range(pdfFileReader.numPages):
    pdfPageObject = pdfFileReader.getPage(pageNum)

    extract_text += pdfPageObject.extractText()

file_object.close()
print(extract_text)
