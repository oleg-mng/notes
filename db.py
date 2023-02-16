import controller
# import aspose.words as aw

def find_in_db(f):
    # global name
    with open('notes.csv', 'r') as data:
            nums = data.readline()
            for nums in data:
                if f in nums:
                    print('Данная заметка найдена: ')
                    print(nums.strip())
                    # doc = aw.Document('directory.txt')
                    # doc.save('name.pdf')

# def print_pdf:
#     pdf_document = "source/YourFile.pdf"
#     with open(pdf_document, "rb") as filehandle:
#     pdf = PdfFileReader(filehandle)
#     info = pdf.getDocumentInfo()
#     pages = pdf.getNumPages()
#     print("Количество страниц в документе: %i\n\n" % pages)
#     print("Мета-описание: ", info)
#     for i in range(pages):
#     page = pdf.getPage(i)
#     print("Стр.", i, " мета: ", page, "\n\nСодержание;\n")
#     print(page.extractText())
            
            
                
