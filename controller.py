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
        with open('notes.csv', encoding='utf-8') as file:
            # file_reader = csv.reader(file, delimiter = ",")
            csv = file.read().splitlines()
            sorted(csv)
            # count = 0
            for row in csv:
                print(row)
        # with open(filename) as file:
        # csv = file.read().splitlines()
        # sorted(csv)
        # for line in csv:
        # item = line.split(',')
        # if  line[0] > '2010-06-08' 
        # print(line)
        
    elif type=='f':
        name = gui.get_value_name()
        db.find_in_db(name)


    
   
