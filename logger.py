from datetime import datetime as dt
from time import time
import csv

x = 0
y = 0
q = 0

def init(a, b, c):
    global x
    global y
    global q
    x = a
    y = b
    q = c

def write():
    with open('notes.csv', 'a') as data:
        data.write(x+', '+y+', '+q)
        data.write('\n')

def rewrite():
    with open('notesTemp.csv', 'w') as data:
        # nums = data.writelines()
        # for nums in data:
        #         if f in nums:
        data.write(x+', '+y+', '+q)
        data.write('\n')
 
        # input = open('notes.csv', 'r')
        # output = open('notesTemp.csv, 'w')
        # writer = csv.writer(output)
        
        # for row in csv.reader(input):
        #     if (row[6] and row[7] and row[8]) != '0':
        #         writer.writerow(row)
        
        # input.close()
        # output.close()


def time_logger():
    with open('log.csv', 'a') as file:
        file.write(dt.strftime(dt.now(), '%m/%d/%Y %H:%M, '))
        file.write(x+', '+y+', '+q)
        # file.write(y)
        # file.write(q)
        file.write('\n')