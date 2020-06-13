import primegen
import pyecm
import time

def findPrimitive(n):
    s = set()
    # находим функцию эйлера
    phi = n - 1

    # факторизуем функцию эйлера
    s = set(pyecm.factors(phi,False,True, 8, 1))
    for r in range(2, phi + 1):
        #Проходимся по всем простым делителям phi
        # и проверяем, если найдена степень равная 1
        flag = False
        for it in s:

            # Проверяем если r^((phi)/primefactors)
            # mod n сравнимо с 1 или нет
            if (pow(r, phi // it, n) == 1):
                flag = True
                break
        # если найден первообразный корень
        if (flag == False):
            return r

            # если не найдено первообразного корня
    return -1




def generate_p_g(dimension):

    p = primegen.get_prime(dimension)
    # g - первообразный корень по модулю p
    g = findPrimitive(p)
    while g==-1:
        p = primegen.get_prime(dimension)
        g = findPrimitive(p)
    return p,g

start_time = time.time()
dimension = 40
a = primegen.get_prime(dimension)
print("Генерируем а - закрытый ключ: ", str(a))
p,g = generate_p_g(dimension)
print("\nГенерируем публичные числа: p - простое число - , g - первообзраный корень по модулю p")
print("p = ", p, "\ng = ", g)
print("\nВычисляем открытый ключ, который шлём клиенту B")
A = pow(g, a, p)
print("А = ", A)
print("\nB принимает публичные p и g от клиента А, а также генерирует свой закрытый ключ b")
b = primegen.get_prime(dimension)
print("Генерируем b - закрытый ключ: ", b)
B = pow(g, b, p)
print("B = ", B)

print("\n\nПубличный ключ К: \nА^b mod p = ", pow(A, b, p))
print("B^a mod p = ", pow(B, a, p))
print("\nЗатраченное время: ", time.time()-start_time, " сек.")
