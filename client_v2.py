# -*- coding: utf-8 -*-
from socket import AF_INET, SOCK_STREAM, socket
import pickle

s = socket(AF_INET, SOCK_STREAM)


def init_socket():
    try:
        s.connect(('localhost', 7777))
    except ConnectionRefusedError:
        print('Соединенте с сервером не установлено')
    except OSError as error:
        print(f'Инициализация не прошла ошибка: {error}')
    else:
        print(f'Соединенте с сервером установлено.')
        return s


def read_messages():
    data = s.recv(1024)
    print(data.decode())


def write_messages():
    while True:
        msg = input('Ваше сообщение: ')
        if msg == 'exit':
            break
        else:
            try:
                return pickle.dumps(msg)
            except pickle.PicklingError:
                print('Не удалось закодировать и отправить сообщни серверу')
            s.close()


def main(ctype):
    if ctype == 'r':
        read_messages()
    elif ctype == 'w':
        write_messages()


if __name__ == '__main__':
    socket = init_socket()
    client_type = input('Вы хотите только чистать (r) или только писать (w)?')
    send = main(client_type)
