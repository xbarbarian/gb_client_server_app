# Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.

word1, word2, word3 = 'разработка', 'сокет', 'декоратор'


word1_unicode, word2_unicode, word3_unicode = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', \
                                              '\u0441\u043e\u043a\u0435\u0442', \
                                              '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'


def check_data(x, y):
    if x == y and type(x) is str:
        return True
    else:
        return False


print(check_data(word1, word1_unicode))
print(check_data(word2, word2_unicode))
print(check_data(word3, word3_unicode))
print(check_data(word2, word3_unicode))
