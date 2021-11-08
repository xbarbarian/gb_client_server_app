"""
3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле
YAML-формата. Для этого:
a. Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке
ASCII (например, €);

b. Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла
с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;

c. Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""

import yaml


def write_yaml(file_name):
    dict_name = {
        'key1': ['test', 123, 'wer1'],
        'key2': 530,
        'key3': {'key4': 785}
    }

    yaml.dump(dict_name, open(file_name, mode='w'), sort_keys=True, indent=4, default_flow_style=False)


def read_yaml(file_name):
    with open(file_name) as f:
        yaml_data = yaml.safe_load(f)
    print(yaml_data)


if __name__ == '__main__':
    try:
        write_yaml('file.yaml')
        read_yaml('file.yaml')
    except Exception as answer:
        print(answer)
