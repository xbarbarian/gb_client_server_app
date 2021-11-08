"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
orders.json. При записи данных указать величину отступа в 4 пробельных символа;

b. Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import json


def write_order_to_json(item, quantity, price, buyer, data):
    basket = {
        'buyer': buyer,
        'data': data,
        'item': item,
        'price': price,
        'quantity': quantity,
    }
    file_name = 'orders.json'
    with open(file_name, 'r+', encoding='utf-8') as f:
        data_json = json.load(f)
        print(data_json)
        data_json["orders"].append(basket)
        print(data_json)
        json.dump(data_json, open(file_name, mode='w', encoding='utf-8'),  sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    try:
        write_order_to_json('carrot', '160', '800', 'IvanovII', '01.01.2021')
        write_order_to_json('carrot2', '260', '2800', 'IvanovII', '01.01.2021')
        write_order_to_json('carrot3', '260', '2800', 'IvanovII', '01.01.2021')
    except Exception as ans:
        print(ans)
