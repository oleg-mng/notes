import controller
import gui
import logger
# import aspose.words as aw

def find_in_db(f):
    # global name
    with open('notes.csv', 'r') as data:
            count = 0
            nums = data.readline()
            for nums in data:
                if f in nums:
                    print('Данная заметка найдена: ')
                    print(nums.strip())
                    count +=1
                    #gui.note_overwriting()
                    #logger.rewrite(x, y, z)
                    #name = gui.get_value_name()
                    #body = gui.get_value_body()
                    #teg = gui.get_value_teg()
            if count==0 : print('Данная заметка не найдена')
                
                

def find_in_db_write(f):
    # global name
    with open('notes.csv', 'a') as data:
            nums = data.readline()
            for nums in data:
                if f in nums:
                    nums.write()
                    

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
            
            
                
