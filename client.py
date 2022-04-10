import socket
from configparser import ConfigParser

parser = ConfigParser()
parser.read("settings.ini")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = parser.get("connect", 'host')
port = 8081
client.connect((host, port))

data = client.recv(1024)   # приветствие
msg = data.decode('utf-8')
print(f'\n\t {msg}')
response = ""
myNumber = -1
while (response != "Верно!"):
    myNumber=input("Введите ваше предполагаемое число в интервале от 1 и до 10:\t")
    try:
        myNumber = int(myNumber)
        if myNumber >= 1 and myNumber <= 10:
            client.send(("guess "+str(myNumber)).encode())
            response = client.recv(1024).decode('utf-8')
            print(response)
        else:
            print('Вы ввели недопустимое значение!')
            continue
    except ValueError:
        continue