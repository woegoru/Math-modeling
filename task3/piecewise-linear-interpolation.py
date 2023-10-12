#Кобяшова Дарья Александровна 3 курс 4 группа

#Написать программы для нахождения промежуточных значений и построить графики функции, заданной в n точках:
#с использованием кусочно-линейного интерполирования:
#При кусочно-линейном интерполировании функция f(x) на интервале xi<=x<=x[i+1]
#(i = 0 ..n-1) аппроксимируется отрезком прямой. Причем, вначале ищем, на каком отрезке 
#[xi, x[i+1]]. находитсяискомая точка х

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
            y_interpol = None
            for j in range(1, len(data[i][0])): #прохождение по одному набору
                x = np.linspace(data[i][0][j - 1], data[i][0][j]) #определение интервала
                a = (data[i][1][j] - data[i][1][j - 1]) / (data[i][0][j] - data[i][0][j - 1]) #вычисление коэффициэнта а
                b = data[i][1][j - 1] - (a * data[i][0][j - 1]) #вычисление коэффициэнта b
                func = a*x + b #вычисление уравнения прямой   
                if x_found < data[i][0][j] and y_interpol == None and x_found >= data[i][0][0]:
                    y_interpol = a*x_found + b #уравнение прямой на которой находится искаомая точка
                plt.plot(x, func, c='k') #соединение точек 
                plt.scatter(x_found, y_interpol, c='r', marker='*', s= 150) #искомая точка
            plt.scatter(data[i][0], data[i][1]) #прохождение по наборам данных
        plt.show()

print('Введите значение x искомой точки')
x_found = float(input())

interpol(data_read('task3/task3.txt'), x_found)