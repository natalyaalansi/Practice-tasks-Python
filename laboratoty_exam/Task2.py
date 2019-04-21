# 2. В последовательности a(n) найти сумму целых элементов, расположенных между
# минимальным и максимальным элементами. (1 балл)
from random import random


def summa():

    # Задаем N рандомных элементов последовательности и выводим на экран
    a = [0]*n
    for i in range(n):
        a[i] = int(random()*50)
        print('%3d' % a[i], end='')
    print()

    min_index = 0
    max_index = 0

    # Поиск индексов минимального и максимального элементов c помошью встроенных функции min() и max()
    # Метод списка index() определяет индекс элемента
    min_index = a.index(min(a))
    max_index = a.index(max(a))
    print(a[min_index], a[max_index])

    # Дополнительное условие чтобы вычислялась сумма между max....min, не только min...max
    if min_index > max_index:
        min_index, max_index = max_index, min_index

    # Вычисляем сумму элементов, стоящих между max....min и min....max
    sum = 0
    for i in range(min_index+1, max_index):
        sum += a[i]
    print(sum)

n = 10
summa()