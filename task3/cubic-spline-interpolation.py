#Кобяшова Дарья Александровна 3 курс 4 группа

#Написать программы для нахождения промежуточных значений и построить графики функции, заданной в n точках:
#с использованием кубического сплайн интерполирования


import matplotlib.pyplot as plt 
import numpy as np
from scipy import interpolate
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
            tck = interpolate.splrep(data[i][0], data[i][1]) #определение сплайна
            x = np.linspace(data[i][0][0], data[i][0][-1]) #определение интервала
            func = interpolate.splev(x, tck) #нахождение значений фуфнкции
            y_interpol = interpolate.splev(x_found, tck) #нахождение значений искомой точки
            plt.plot(x, func, c='k') #соединение точек 
            if x_found >= min(data[i][0]) and x_found <= max(data[i][0]):
                plt.scatter(x_found, y_interpol, c='r', marker='*', s= 150) #искомая точка
            plt.scatter(data[i][0], data[i][1]) #прохождение по наборам данных
        plt.show()

print('Введите значение x искомой точки')
x_found = float(input())

interpol(data_read('task3/task3.4.txt'), x_found)