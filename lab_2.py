from random import randint
from math import pi
import time

# Число испытаний
M = 10000
# Максимальное число
N = 10**100
print('N = ' + str(N))

# Функция принимает на вход два числа
# Алгоритм реализован методом деления с остатком
# Функция возвращает 1 если числа взаимнопростые,
# иначе возвращает 0
def gcd(a, b):
	i = 0
	while a != 0 and b != 0:  # завершаем алгоритм, когда остаток равен 0
		if a > b:
			a = a % b
		else:
			b = b % a
		i += 1
	if (a+b) == 1:  # у взаимно простых чисел НОД=1
		return 1
	else:
		return 0


summ = 0
i = 0
start_time = time.time() # засекаем текущее время
while i < M:
	a = randint(1, N)	# Рандомно выбираем два числа a и b из отрезка от 1 до N
	b = randint(1, N)
	summ += gcd(a,b)	# суммируем все случае взаимной простоты чисел (qcd(,) = 1)
	i += 1


probability = summ/M 	# Оценим вероятность получения пары взаимно
                        # простых чисел

print('Секунды = '+str(time.time()-start_time))
print()
print('Вероятность = ' + str(probability))
print()
print('Теоретическая оценка:')
print()
print(6/pi**2)