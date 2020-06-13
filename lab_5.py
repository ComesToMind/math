import time
from sympy.ntheory import totient
from sympy.core.numbers import igcd

N = 2019
a = 2019
z = 10**2019
start_time = time.time()
aa = a # начальное значение основания есть 2019
for i in range(N-1):
	r = aa % totient(z) # метод totient высчитывает функцию эйлера
	aa = pow(a,r,z) # a^r (mod z)
print(aa)
print('Затраченное время = ', time.time()-start_time)