# Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию. Принудительно открыть файл
# в формате Unicode и вывести его содержимое
from chardet.universaldetector import UniversalDetector
import io

detector = UniversalDetector()
list_data = ['сетевое программирование', 'сокет', 'декоратор']

# Создаем файл
with open('file.txt', 'w+') as new_file:
    for i in list_data:
        new_file.write(i + '\n')

# Проверяем кодировку файла
with open('file.txt', 'rb') as new_file:
    for i in new_file:
        detector.feed(i)
        if detector.done: break
detector.close()
print(detector.result)

# Принудительно открыть файл в формате Unicode и вывести его содержимое
f_n = io.open('file.txt', mode='r', encoding='utf-8', errors='ignore')
print(f_n.read())
