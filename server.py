import socket
from configparser import ConfigParser
import random
import threading

parser = ConfigParser()
parser.read("settings.ini")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = parser.get("connect", 'host')
port = 8081
server.bind((host, port))


def connect_client(conn, addr):
    print(f"Внешнее соединение по IP {addr[0]} порта {addr[1]}. \n")
    conn.send(f'Вы успешно подключены к серверу «Угадай число» \n'
              f'Вам необходимо угадать число загаданное сервером от одного до десяти.'.encode('utf-8'))
    server_number = random.randint(1, 10)
    client_number = 100
    while client_number != server_number:
        client_number = int(conn.recv(1024).decode('utf-8')[6:])
        if server_number == client_number:
            conn.send('Верно!'.encode('utf-8'))
        if server_number < client_number:
            conn.send('Сервер загадал число меньше...'.encode('utf-8'))
        if server_number > client_number:
            conn.send('Сервер загадал число больше...'.encode('utf-8'))
    print(f"Внешнее соединение по IP {addr[0]} порта {addr[1]} завершено. \n")
    conn.close()


def start():
    server.listen(4)
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=connect_client, args=(conn, addr))
        thread.start()
        print(f"Активных подключений: {threading.active_count() - 1}.\n")


print("Запуск сервера...")
print(f'Сервер включён по IP {host} на порту {port}')
start()
