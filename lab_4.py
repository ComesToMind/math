import gmpy2 # для ускорение pyecm без него будет работать крайне долго
import pyecm # для факторизации
from random import randint
import time
from math import pi


def is_square_free(n):
	multipliers_list = list(pyecm.factors(n,False,True, 8, 1)) # данная функция факторизирует число n
	# описание библиотеки pyecm https://github.com/martingkelly/pyecm/blob/master/pyecm.py
	for i in range(len(multipliers_list)-1): # просматриваем уже с
		if multipliers_list[i] == multipliers_list[i+1]:
			return False # смотрим, если два числа в массиве равны - то это квадрат
	return True

N = 10**50

M = 1000

summ = 0 # здесь кол-во свободных от квадратов чисел от 1000 итераций

start_time = time.time()

for i in range(M):
	a = randint(1,N)
	print(a)
	if is_square_free(a):
		summ += 1
	else:
		summ += 0

print()
print("Результат программы: " + str(summ/M))
print("Теоретическая оценка:  " + str(6/pi**2))
print("Время работы программы: " + str(time.time()-start_time))
