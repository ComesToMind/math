import primegen
import pyecm
import time
import  random
from colorama import Fore
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

def encrypt(message,y,p,g):
    cipher = []
    for char in message:
        k = random.randint(1,p-1)
        a = pow(g,k,p)
        b = (pow(y,k,p)*ord(char))%p
        cipher.append((a,b))
    return cipher

def decrypt(message,x,p):
    decrypted_text = []
    for char in message:
        symp = pow(char[0],(p-1-x),p)
        symp = (char[1]*symp)%p
        decrypted_text.append(chr(symp))
    return decrypted_text
start_time = time.time()
dimension = 80
p,g = generate_p_g(dimension)
print(Fore.YELLOW+"Генерируем числа: p - простое число - , g - первообзраный корень по модулю p")
print(Fore.CYAN+"p = ", p, "\ng = ", g)
x = random.randint(1,p-1)
print(Fore.YELLOW+"\nФормируем закрытый ключ х! \nВыбираем случайное целое число x из отрезка 1 < x < p-1 : ", x)
y = pow(g, x, p)
print(Fore.YELLOW+"\nВычисляем y = g^x mod p) = ",y)
print("Клиенту B шлем y = ", y, "g = ", g,"\nОн шифрует сообщение.")
plain = input("Введите сообщение: ")
print(Fore.YELLOW+"\nПроцесс шифрования...")
cipher = encrypt(plain,y,p,g)
print(Fore.CYAN+"\nЗашифрованное сообщение посимвольно парами чисел (a,b):")
for ind in cipher:
    print(ind)
print(Fore.YELLOW+"\nЗная закрытый ключ x, исходное сообщение можно вычислить из шифротекста (a,b)")
print("По формуле M = b*a^(p-1-x) mod p")

decrypted_text = decrypt(cipher,x,p)

print(Fore.CYAN+"\n", "".join(decrypted_text))
