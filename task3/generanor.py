#Генератор рандомных координат для файла

from random import uniform

x = 0
y = 0
max_step = 5
min_step = 1
 
with open('task4/task4.txt', 'w') as file: #открытие файла с записью
    for _ in range(20):
        x += uniform(min_step, max_step) #задание точек х
        file.write(str(x) + ', ') #запись х в файл
    x += uniform(min_step, max_step) #добавление последнего х без разделителя
    file.write(str(x))
    file.write('\n')
    for _ in range(20):
        y = uniform(0, 50) #задани точек у
        file.write(str(y) + ', ') #запись н в файл
    y = uniform(0, 50) #добавление последнего у без разделителя
    file.write(str(y))
    file.write('\n')



