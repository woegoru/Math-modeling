#Кобяшова Дарья Александровна 3 курс 4 группа

#Написать программы для нахождения промежуточных значений и построить графики функции, заданной в n точках:
#с использованием кусочно-параболического интерполирования.
#При кусочно-параболическом интерполировании полином строится на интервале [𝑥𝑖−1, 𝑥𝑖, 𝑥𝑖+1] по 3-м узловым точкам, 
#ближайшим к заданному значению аргумента.

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
            for j in range(1, len(data[i][0])-1, 2): #прохождение по одному набору
                x = np.linspace(data[i][0][j - 1], data[i][0][j + 1]) #определение интервала
                matrix_coef = np.array([
                            [(data[i][0][j - 1])**2, data[i][0][j - 1], 1.],
                            [(data[i][0][j])**2, data[i][0][j], 1.],
                            [(data[i][0][j + 1])**2, data[i][0][j + 1], 1.]
                            ]) #матрица (левая часть системы)
                free_member = np.array([data[i][1][j - 1], data[i][1][j], data[i][1][j + 1]]) #свободные члены (правая часть системы)
                decision = np.linalg.solve(matrix_coef, free_member) #решение системы
                func = (decision[0]*x**2 + decision[1]*x + decision[2]) #вычисление уравнения параболы   
                if x_found < data[i][0][j + 1] and y_interpol == None and x_found >= data[i][0][0]:
                    y_interpol = decision[0]*x_found**2 + decision[1]*x_found + decision[2] #уравнение прямой на которой находится искаомая точка
                plt.plot(x, func, c='k') #соединение точек 
                plt.scatter(x_found, y_interpol, c='r', marker='*', s= 150) #искомая точка
            plt.scatter(data[i][0], data[i][1]) #прохождение по наборам данных
        plt.show()

print('Введите значение x искомой точки')
x_found = float(input())

interpol(data_read('task3/task3.2.txt'), x_found)