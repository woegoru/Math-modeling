#Генератор рандомных координат для файла

from random import uniform

x = 0
y = 0
max_step = 5
min_step = 1
 
with open('task4/task4.txt', 'w') as file:
    for _ in range(20):
        x += uniform(min_step, max_step)
        file.write(str(x) + ', ')
    x += uniform(min_step, max_step)
    file.write(str(x))
    file.write('\n')
    for _ in range(20):
        y = uniform(0, 50)
        file.write(str(y) + ', ')
    y = uniform(0, 50)
    file.write(str(y))
    file.write('\n')