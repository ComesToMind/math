from random import randint
from math import log
import time

# Число испытаний
M = 10000
# Максимальное число
N = 10**100


print('N = ' + str(N))

# Функция проверяющая остаток от деления r на условие b/2
def remainder_of_division(b,N):
	if (N % b) < b/2:
		return 1
	else:
		return 0


summ = 0
i = 0
start_time = time.time()
for i in range(i, M):
	b = randint(1, N)					# Рандомно выбираем b из отрезка от 1 до N
	summ += remainder_of_division(b,N)	# Проверяем условие


probability = summ/M #  Рассчёт вероятности

print('Секунды = '+str(time.time()-start_time))
print()
print('Практическая вероятность = ' + str(probability))
print()
print('Теоретическая оценка вероятности = '+str(2-2*log(2)))

