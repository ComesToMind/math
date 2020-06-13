from random import randint
from math import log, pi
import time


# Число испытаний
M = 10000

# Максимальное число
N = 10 ** 100

print('N = ' + str(N))

# принимает на вход два числа
# Алгоритм реализован методом деления с остатком
# Функция также возвращает кол-во иттераций алгоритма Евклида
def gcd(a, b):
    itterations = 0
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
        itterations += 1

    return itterations


summ = 0
i = 0
start_time = time.time()  # засекаем текущее время
for i in range(i, M):
    a = randint(1, N)  # Рандомно выбираем два числа a и b из отрезка от 1 до N
    b = randint(1, N)
    summ += gcd(a, b)  # Суммируем
    i += 1

# Получаем среднее кол-во итераций при M опытах
avg = summ / M
print('Секунды = ' + str(time.time() - start_time))
print()
print('Среднее количество операций = ', avg)
print()
print('Теоретическая оценка кол-ва операций = ' + str(12 * log(2) * log(N) / pi ** 2))
