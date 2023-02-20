import gui
import logger
import db
import csv

def button_click():
    global name
    global body
    global teg
    type=gui.var_of_operation()

    if type=='w':
        name = gui.get_value_name()
        body = gui.get_value_body()
        teg = gui.get_value_teg()
        logger.init(name, body, teg)
        logger.time_logger()
        result = gui.type_of_operation()

    elif type=='r':
        with open('log.csv', encoding='utf-8') as file:
            # file_reader = csv.reader(file, delimiter = ",")
            csv = file.read().splitlines()
            # sorted(csv)
            csv.sort()
            # count = 0
            for row in csv:
                print(row)
        
    elif type=='f':
        name = gui.get_value_name()
        db.find_in_db(name)
        


    
   
