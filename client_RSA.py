import socket

def encrypt(key,n, plaintext):
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(pow(ord(char), key, n)) for char in plaintext]
    #Return the array of bytes
    return cipher


def get_data(sock):
    buf = ''
    while ' ' not in buf:
        buf += sock.recv(1).decode('utf8')
    return buf

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# conn, addr = sock.accept()

sock.connect(('localhost',14012))
e = int(get_data(sock))
n = int(get_data(sock))
print("Публичные ключ:\n(", e, n, ")")
message = input("Введите ваще сообщение: ")
cipher = encrypt(e,n,message)
print("Сообщение зашифровано!")
print(cipher)
print(" Отправка на сервер...")

# отправляем число всех символов на всякий случай ошибок
sock.send(bytes((str(len(cipher))+' '),'utf8'))

for k in cipher:
    sock.send(bytes(str(k) + ' ', 'utf8'))

input("\nОтправлено!\nНажмите любую клавищу для выхода...")
sock.close()