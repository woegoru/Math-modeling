#Кобяшова Дарья Александровна 3 курс 4 группа

#Программа для аппроксимации таблично заданной функции алгебраическим полиномом 
#по методу наименьших квадратов. 
#Для тестирования программы в качестве исходной информации можно задать несколько точек параболы
#n-й степени и посмотреть, получаются ли в результате вычислений те же коэффициенты

import matplotlib.pyplot as plt 
import numpy as np
from random import uniform

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

def mnk(data, degree, k):
    matrix_coef = [] #матрица (левая часть системы)
    free_member = [] #свободные члены (правая часть системы)
    for i in range(len(data)):
        for v in range(degree + 1):
            left_str_of_matrix = [] #строка матрицы
            for k in range(degree + 1): 
                left_str_of_matrix.append(sum([x**(v + k) for x in data[i][0]])) #сбор строки матрицы
            matrix_coef.append(left_str_of_matrix)
            free_member.append(sum([data[i][1][k] * (data[i][0][k]**v) for k in range(len(data[i][0]))]))
        left = np.array(matrix_coef) #запись коэффициэнтов левой части
        right = np.array(free_member) #запись коэффициэнтов правой части
        coef = np.linalg.solve(left, right) #решение системы линейных уравнений
        print('\nВычисленные коэффициэнты:')
        for s in range(k+1):
            print(f'C{s} = ', "{:.4f}".format(coef[s], ".55f"),  sep='')
    return coef

def calc_poly(degree, coef, x):
    y = 0
    for n in range(degree + 1):
        y += coef[n] * x**n #функция полинома
    return y #возврат функции для дальнейшего использования

def calc_error(data, degree, coef):
    error = 0
    for i in range(len(data)):
        for j in range(len(data[i][0])):
            error += (abs(calc_poly(degree, coef, data[i][0][j]) - data[i][1][j]))**2
    print('\nСуммарная ошибка отклонения:', error)

def data_draw(data): #определение функции изображения графика
    for i in range(len(data)):
        plt.scatter(data[i][0], data[i][1])

def print_poly(degree): #определение функции создания многочлена по степени введенной пользователем
    y_pol = ''
    x_pol = 'x'
    for k in range(degree + 1): #вычислеение многочлена
        if k == 0: #если степень 0
            y_pol += 'C' + str(k)
            if degree > k:
                y_pol += ' + '
        if k == 1: #если степень 1
            y_pol += 'C' + str(k)+ ' * ' + str(x_pol)
            if degree > k:
                y_pol += ' + '
        if k > 1: #если степень больше 1
            y_pol += 'C' + str(k) + ' * ' + str(x_pol) + '^' + str(k)
            if degree > k:
                y_pol += ' + '
    print('Так выглядит ваш многочлен: y =', y_pol)
    return(k)

def generator(path: str, x_min, x_max, max_step, min_step, par, err, a, b, c):
    x = x_min
    with open(path, 'w') as file: #открытие файла с записью
        x_ = [x]
        file.write(str(x) + ', ')
        while x <= x_max - max_step:
            x += uniform(min_step, max_step) #задание точек х
            x_.append(x)
            file.write(str(x) + ', ') #запись х в файл
        x_.append(x_max)
        file.write(str(x_max))
        file.write('\n')
        for i in range(len(x_)-1):
            y = a*x_[i]**(par)+ b*x_[i]**(par-1) + c + uniform(-err, err)  #задани точек у
            file.write(str(y) + ', ') #запись н в файл
        y = a*x_[-1]**(par) + b*x_[-1]**(par-1) + c + uniform(-err, err) #добавление последнего у без разделителя
        file.write(str(y))
        file.write('\n')
        print('(ДЛЯ ПРОВЕРКИ: исходно заданы коэффициэнты:', c, b, a, ')')
        print('---------------------------')


degree = int(input('Введите степень многочлена: '))
print('---------------------------')

x_max = 20
x_min = -20
path = 'task4/task4.txt'

generator(path = path,
          x_min = x_min,
          x_max = x_max,
          max_step = 2,
          min_step = 0.5,
          par = 2,
          err = 10,
          a = 3,
          b = 7,
          c = 4,
          #d = 0,
          #e = 0
          )



k = print_poly(degree)
data = data_read(path)
poly_coef = mnk(data, degree, k)
x_linespace = np.linspace(x_min, x_max)




#print_poly(degree)
data_draw(data)
calc_error(data, degree, poly_coef)


plt.plot(x_linespace, calc_poly(degree, poly_coef, x_linespace), c='r')
plt.show()