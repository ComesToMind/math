from gmpy2 import is_prime, f_div, mpz, mul, mpfr, is_odd, powmod, next_prime
from random import random
def get_prime(dimension : int):
    dim = dimension
    start_prime = 1351
    repit_flag = True
    p = mpz(start_prime)
    while p.num_digits() <= dim:
        if repit_flag:
            repit_flag = False
            # Используется теорема Диемитко https://studfile.net/preview/6268704/page:28/
            # Она позволяет строить большие числа на основе существуюших меньших простых чисел
            # n=qR+1, где q – простое число, R – четное, R<4(q+1).
            # Высчитаем число N
            N = f_div(mpz(10 ** (dim - 1)), mpz(start_prime)) + f_div(mpz(10 ** (dim - 1) * mpfr(random())),mpz(start_prime))
            # Если оно нечетное, то добавляем 1
            N = N + 1 if is_odd(N) else N
            U = 0
            # получаем число и проверяем его на условие теоремы
        p = (N + U) * start_prime + 1
        # если условия выполнены, то ищем новое простое число для расчета
        if pow(2, p - 1, p) == 1 and pow(2, N + U, p) != 1:
            return int(p)
        else:
            U += 2
