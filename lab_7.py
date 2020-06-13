from time import time
from gmpy2 import is_prime, f_div, mpz, mul, mpfr, is_odd, powmod, next_prime
from random import random


#Начальное простое число
start_prime = 14312537157963352796505350926163762201400602486571381002666563262556612376406142848247396572048886107336187167342694341985829323860469455621684312636442867271907923647000306009850899429502488393513134547503608363245680702515431422208639433785139559675467356347654186879125838866687061735064279905407481146588832248724898053718844430067509962804838597719337098576579845704762986759374241419485164400275811074844897884943545504153765985729817933773093367667537621605201694081737902741381682510827487133
start_time = time()
current_number = mpz(start_prime)
current_prime = start_prime
list_primes = []
p = mpz(start_prime)
repit_flag = True

#задаем порядок чисел для поиска
dim = 10**20000

U = 0


# пока число имеет порядок меньше задаваемого
while p.num_digits() <= dim:
    if repit_flag:
        repit_flag = False
        # Используется теорема Диемитко https://studfile.net/preview/6268704/page:28/
        # Она позволяет строить большие числа на основе существуюших меньших простых чисел
        # n=qR+1, где q – простое число, R – четное, R<4(q+1).
        # Высчитаем число N
        print(1)
        N = f_div(mpz(10 ** (dim - 1)), mpz(current_prime)) + f_div(mpz(10 ** (dim - 1) * mpfr(random())), mpz(current_prime))
        print(2)
        # Если оно нечетное, то добавляем 1
        N = N + 1 if is_odd(N) else N
        U = 0
        # получаем число и проверяем его на условие теоремы
    p = (N + U)*current_prime + 1
    print(p)
    # если условия выполнены, то ищем новое простое число для расчета
    if pow(2,p-1,p) == 1 and pow(2,N+U,p) != 1:
        print(p)
        repit_flag = True
        break
    else:
        U += 2

print()
print("Общее время:" + str(time()-start_time))
summ = 0
# Дополнительная проверка на простоту встроенной функцией gmpy2 is_prime()
for i in list_primes:
    if is_prime(i):
        summ += 1
print()
print(summ)