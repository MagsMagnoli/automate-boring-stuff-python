import PyPDF2

pdfFile = open('file.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)
writer = PyPDF2.PdfFileWriter()
for pageNum in range(reader.numPages):
    page = reader.getPage(pageNum)
    writer.addPage(page)
outputFile = open('output.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdfFile.close()
