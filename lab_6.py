from time import time
from gmpy2 import is_prime, f_div, mpz, mul, mpfr, is_odd, powmod, next_prime
from random import random


#Начальное простое число
start_prime = 3571
start_time = time()
current_number = mpz(start_prime)
current_prime = start_prime
list_primes = []
p = mpz(start_prime)
repit_flag = True

#задаем порядок чисел для поиска
dim = 500

U = 0

for i in range(1000):
    print(i)
# пока число имеет порядок меньше задаваемого
    while p.num_digits() <= dim:
        if repit_flag:
            repit_flag = False
            # Используется теорема Диемитко https://studfile.net/preview/6268704/page:28/
            # Она позволяет строить большие числа на основе существуюших меньших простых чисел
            # n=qR+1, где q – простое число, R – четное, R<4(q+1).
            # Высчитаем число N
            N = f_div(mpz(10 ** (dim - 1)), mpz(current_prime)) + f_div(mpz(10 ** (dim - 1) * mpfr(random())), mpz(current_prime))
            # Если оно нечетное, то добавляем 1
            N = N + 1 if is_odd(N) else N
            U = 0
            # получаем число и проверяем его на условие теоремы
        p = (N + U)*current_prime + 1
        # если условия выполнены, то ищем новое простое число для расчета
        if pow(2,p-1,p) == 1 and pow(2,N+U,p) != 1:
            print(p)
            list_primes.append(p)
            repit_flag = True
            break
        else:
            U += 2
current_prime = next_prime(current_prime)

print()
print("Общее время:" + str(time()-start_time))
summ = 0
# Дополнительная проверка на простоту встроенной функцией gmpy2 is_prime()
for i in list_primes:
    if is_prime(i):
        summ += 1
print()
print(summ)