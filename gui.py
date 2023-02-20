import db
import logger


def get_value_name():
    global name
    name = str(input('Введите заголовок заметки:  '))
    return name


def get_value_body():
    global body
    body = str(input('Введите тело заметки: '))
    return body


def get_value_teg():
    global teg
    teg = str(input('Введите тег: '))
    print('Заметка успешно сохранена')
    return teg


def type_of_operation():
    global result
    result = logger.write()
    return result

def type_rewrite():
    global result
    result = logger.rewrite()
    return result

def var_of_operation():
    global var
    var = input('какую операцию вы хотите сделать в справочнике (w/r/f)?: ')
    # if op == 'w':
    #     var = math_f.write()
    # elif op == 'r':
    #      result = math_f.read()
    return var

def note_overwriting():
    global over
    over = input('хотите внести изменения в данную заметку (y/n)?: ')
    if over == 'y':
        name = get_value_name()
        body = get_value_body()
        teg = get_value_teg()
        logger.init(name, body, teg)
        logger.time_logger()
        result = type_of_operation()

        # logger.write()
        # logger.time_logger()
    elif over == 'n':
         exit
    return over