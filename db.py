import controller
import gui
import logger
import csv
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
                    gui.note_overwriting()
                    # result = logger.rewrite()
                    #name = gui.get_value_name()
                    #body = gui.get_value_body()
                    #teg = gui.get_value_teg()
            if count==0 : print('Данная заметка не найдена')
                
