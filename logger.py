from datetime import datetime as dt
from time import time

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

def time_logger():
    with open('log.csv', 'a') as file:
        file.write(dt.strftime(dt.now(), '%m/%d/%Y %H:%M, '))
        file.write(x)
        file.write('\n')
        




