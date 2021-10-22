#  4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
# в байтовое и выполнить обратное преобразование (используя методы encode и decode).

list_data = ['разработка', 'администрирование', 'protocol', 'standard']


def encode_data(args):
    return args.encode('utf-8')


def decode_data(args):
    return bytes.decode(args, 'utf-8')


data = []
for i in list_data:
    data.append(encode_data(i))
print(data)

for i in data:
    print(decode_data(i))
