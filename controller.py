import gui
import logger
import db
import csv


def button_click():
    global name
    global surname
    global mobile
    type=gui.var_of_operation()
    if type=='w':
        name = gui.get_value_name()
        surname = gui.get_value_surname()
        mobile = gui.get_value_mobile()
        logger.init(name, surname, mobile)
        logger.time_logger()
        result = gui.type_of_operation()
    elif type=='r':
        with open('notes.csv', encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter = ",")
            count = 0
            for row in file_reader:
                print(f'{row[0]}, {row[1]}, {row[2]}')
            count += 1
            print(f'Всего в файле {count} строк.')
        # with open('notes.csv') as f:
        # reader = csv.reader(f)
        # for row in reader:
        # print(row)
        
    elif type=='f':
        name = gui.get_value_name()
        db.find_in_db(name)


    
   
