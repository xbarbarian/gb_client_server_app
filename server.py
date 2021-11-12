""""
1. Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
клиент отправляет запрос серверу;
сервер отвечает соответствующим кодом результата.
Клиент и сервер должны быть реализованы в виде отдельных скриптов, содержащих соответствующие функции.
Функции клиента:

сформировать presence-сообщение;

отправить сообщение серверу;
получить ответ сервера;
разобрать сообщение сервера;
параметры командной строки скрипта client.py <addr> [<port>]:
addr — ip-адрес сервера;
port — tcp-порт на сервере, по умолчанию 7777.
Функции сервера:
принимает сообщение клиента;
формирует ответ клиенту;
отправляет ответ клиенту;
имеет параметры командной строки:
-p <port> — TCP-порт для работы (по умолчанию использует 7777);
-a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).

Задание:
1.) Изменить имена переменных и функций в предоставленном скрипте (чем больше, тем лучше);
2.) Изменить порядок пары ip_адрес-порт на порт-ip_адрес : <port> [<addr>]:
3.) Добавить в сообщение от клиента номер порта, по которому запрашиватеся соединение, например:
` {'action': 'presence', 'time': 1634873801.598524, 'port': 9000, 'user': {'account_name': 'Guest'}}
"""

from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, socket
import pickle
import time

HOST = '127.0.0.1'
PORT = 7777
SERVER_SOCKET = socket(AF_INET, SOCK_STREAM)


def init_socket():
    SERVER_SOCKET.bind((HOST, PORT))
    SERVER_SOCKET.listen(6)
    SERVER_SOCKET.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)


def main():
    while True:
        client, addr = SERVER_SOCKET.accept()
        print('Получен запрос на соединение от %s' % str(addr))
        data = client.recv(1024)
        response = {
            'response': 200,
            'alert': 'Connect Success',
            'time': time.time(),
            'user': ''
        }
        client.send(pickle.dumps(response))

        client.close()


if __name__ == '__main__':
    SOCKET = init_socket()
    try:
        main()
    except Exception as text:
        print('Сервер не запустился')
