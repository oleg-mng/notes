import db
import logger


def get_value_name():
    global name
    name = str(input('Введите заголовок заметки:  '))
    return name


def get_value_surname():
    global surname
    surname = str(input('Введите тело заметки: '))
    return surname


def get_value_mobile():
    global mobile
    mobile = str(input('Введите тег: '))
    return mobile


def type_of_operation():
    global result
    result = logger.write()
    return result

def var_of_operation():
    global var
    var = input('какую операцию вы хотите сделать в справочнике (w/r)?: ')
    # if op == 'w':
    #     var = math_f.write()
    # elif op == 'r':
    #      result = math_f.read()
    return var