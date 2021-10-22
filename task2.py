# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

import codecs


def check_data(*args):
    for arg in args:
        print(f" type: {type(arg)},length:{len(arg)} {str(arg, 'utf-8')}")


check_data(b'class', b'function', b'method')
