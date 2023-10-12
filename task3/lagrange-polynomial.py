#Кобяшова Дарья Александровна 3 курс 4 группа

#Написать программы для нахождения промежуточных значений и построить графики функции, заданной в n точках:
#посредством построения полинома Лагранжа.
#Многочлен Лагранжа ищется в виде линейной комбинации из значений 𝑦 = 𝑓(𝑥) в 𝑖-ых узлах интерполяции и специально построенных 
#из системы узлов интерполяции многочленов 𝐿𝑛(𝑥) 𝑛 -ой степени


import matplotlib.pyplot as plt 
import numpy as np
from generanor import *

def data_read(path: str): #определение функции чтения данных из файла
    f = open(path, 'r')
    l = f.readline() #чтение первой строки
    data = list()
    while(l):
        x = [float(num) for num in l.split('\n')[0].split(', ')] #получение из строки список чисел для х
        l = f.readline() #чтение второй строки
        y = [float(num) for num in l.split('\n')[0].split(', ')] #получение из строки список чисел для у
        data.append([x, y])
        l = f.readline() #чтение строки-разграничителя
        l = f.readline() #чтение следующей(новой первой) строки
    return data

def interpol(data, x_found):
        for i in range(len(data)):
            func = 0
            y_interpol = 0
            x = np.linspace(data[i][0][0], data[i][0][-1]) #определение интервала
            for j in range(len(data[i][0])): #прохождение по одному набору
                numerator = 1
                numerator_ = 1
                denominator = 1 
                for k in range(len(data[i][0])):
                    if k != j:
                        numerator *= x - data[i][0][k] #выисление числителя
                        numerator_ *= x_found - data[i][0][k] #выисление числителя
                        denominator *= data[i][0][j] - data[i][0][k] #вычисление знаменателя
                func += data[i][1][j] * (numerator/denominator) #вычисление многочлена Лагранжа   
                y_interpol += data[i][1][j] * (numerator_/denominator)
            plt.plot(x, func, c='k') #соединение точек 
            if x_found >= min(data[i][0]) and x_found <= max(data[i][0]):
                plt.scatter(x_found, y_interpol, c='r', marker='*', s= 150) #искомая точка
            plt.scatter(data[i][0], data[i][1]) #прохождение по наборам данных
        plt.show()

print('Введите значение x искомой точки')
x_found = float(input())

interpol(data_read('task3/task3.3.txt'), x_found)