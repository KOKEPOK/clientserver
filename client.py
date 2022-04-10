import socket
from configparser import ConfigParser

parser = ConfigParser()
parser.read("settings.ini")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = parser.get("connect", 'host')
port = 8081
client.connect((host, port))

msg = client.recv(1024).decode('utf-8') # приветствие
print(f'\n\t {msg}')
answer = ""
client_number = 100
while answer != "Верно!":
    try:
        client_number = int(input("Введите ваше предполагаемое число в интервале от 1 и до 10:\t"))
        if client_number >= 1 and client_number <= 10:
            client.send(("guess "+str(client_number)).encode('utf-8'))
            answer = client.recv(1024).decode('utf-8')
            print(answer)
        else:
            print('Вы ввели недопустимое значение!')
            continue
    except ValueError:
        continue