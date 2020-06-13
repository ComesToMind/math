from gmpy2 import is_prime, f_div, mpz, mul, mpfr, is_odd, powmod, next_prime
from random import random
import socket

import re
# def is_good_input(inputs)
#     if re.fullmatch('[0-9]*', inputs) and inputs:
#         return True

def p_and_q():
    dim = 100
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

def multiplicative_inverse(a, b):
    save = b
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    if(x<0):
        x +=save
        return x
    return x

def key_generation():
    print("Генерируем публичный и приватный ключи . . .")
    q = p_and_q()
    p = p_and_q()
    n = q*p
    phi = (q-1)*(p-1)
    # d*e _= 1 mod phi
    public_exponent = 65537
    secret_exponent =multiplicative_inverse(public_exponent,phi)
    return ((public_exponent,n), (secret_exponent,n))



def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(pow((char), key, n)) for char in ciphertext]
    return plain

def get_data(sock):
    buf = ''
    while ' ' not in buf:
        buf += sock.recv(1).decode('utf8')
    return buf

def key_inputs():
    flag = True
    print("Числа будут проверены на простоту!")
    while flag:
        p = int(input("Введите P: "))
        q = int(input("Введите q: "))
        if not is_prime(mpz(p)) or not is_prime(mpz(q)):
            print("p и q не являются простыми числами!")
            continue
        flag = False
    n = q*p
    phi = (q-1)*(p-1)
    flag = True

    while flag:
        print("Введите e от 1 до ",phi , " (удобные числа 17, 257 и 65537): ")
        e = int(input())
        if (not is_prime(mpz(e))) or (e <= 1) or (e>= phi):
            print("e не являются простым числом или лежит вне допустимого промежутка!")
            flag = True
            continue
        flag = False
        secret_exponent = multiplicative_inverse(e, phi)
        if  (not is_prime(mpz(secret_exponent)))  or secret_exponent==1 or secret_exponent <0:
            print("Уппс, при данном значении открытой экспоненты ключи d и e совпадают или d = 1 !")
            flag = True
            continue

        return ((e, n), (secret_exponent, n))

print("Это сервер RSA")
print("Здесь происходит расшифрование сообщения от клиента!")

flag = False
while flag != True:
    print("Выберите режим ввода ключа: \n(1).Генерация \n(2). Ручной ввод ")
    inputs = input("Ваш выбор: ")
    if inputs == "":
        continue
    if inputs=='1':
        public, private = key_generation()
        flag = True
    elif inputs=='2':
        public, private = key_inputs()
        flag = True
    else:
        c = input("Выйти из программы?[y/n]")
        if c == 'y':
            exit(0)


print("Ваш публичный ключ:\n",public, "\nВаш приватный ключ:\n ", private)

print("Ожидаем соединение с клиентом: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost',14012))
sock.listen(1)
conn, addr = sock.accept()
print("Есть подключение с:", addr)
print("Отправка публичного ключа клиенту")
num = str(public[0])+' '
conn.send(bytes(num, 'utf8'))
conn.send(bytes((str(public[1])+' '),'utf8'))
print("Ждём зашифрованное сообщение от клиента...")

count_of_synmols = int(get_data(conn))

recieved_list = []
for i in range(0,count_of_synmols):
    recieved_list.append(int(get_data(conn)))
print("\nЗашифрованное сообщение публичным ключом: ")
print(recieved_list)
decrypted = decrypt(private,recieved_list)

print("\n\nРасшифрованное сообщение: ")
print(''.join(decrypted))
input("Нажмите любую клавищу для выхода...")