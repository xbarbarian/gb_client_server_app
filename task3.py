# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

list = [b'attribute', b'класс', b'функция', b'type']


def check_data(args):
    return args


for i in list:
    print(check_data(i))

# все слова в кирилическом формате выдают ошибку - 'SyntaxError: bytes can only contain ASCII literal characters'
