import db
import logger

def get_value_name():
    global name
    name = str(input('Введите заголовок заметки: '))
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
    return var

def note_overwriting(s):
    global over
    over = input('хотите внести изменения в данную заметку (y/n)?: ')
    if over == 'y':
        name = get_value_name()
        body = get_value_body()
        teg = get_value_teg()
        logger.init(name, body, teg)
        print('Новые данные для заметки - '+name+', '+body+', '+teg+'- изменения занесены в db')
        
        with open('notes.csv', 'r') as file:
            with open('notesTemp.csv', 'w') as data:
                nums = file.readline()
                data.write('\n')
                for nums in file:
                    if s in nums:
                        # data.write('\n')
                        # print(nums.strip())
                        # k = name+', '+body+', '+teg
                        data.write(name+', '+body+', '+teg)
                        data.write('\n')
                        # print(k)
                        continue
                    data.write(nums)
                    # print(nums)
        print('изменения в db внесены')

        with open('notesTemp.csv', 'r') as file:
            with open('notes.csv', 'w') as data:
                nums = file.readline()
                data.write('\n')
                for nums in file:
                    data.write(nums)
                    # data.write('\n')
            
                    
        logger.time_logger()
        
    elif over == 'n':
        exit
    return over