'''
Created on Jul 8, 2018

@author: pedroc.f.santos
'''

from datetime import date
from datetime import time

def capture_input() :
    nome = raw_input()
    print('Voce digitou ' + nome)
    return nome

def calculate_age() :
    print('De Recife, ' + str(time.hour) + 'h'+ str(time.minute) + 'm'+ str(time.second) + 's')
    print('De Recife, ' + str(date.today().day) + ' de ' + str(date.today().month) + ' de ' + str(date.today().year))
    number = int( capture_input() )
    idade = date.today().year - number
    return idade