def int_func(word):
    """Функция делает заглавной каждую первую букву слова в строке, а остальные делает строчными"""
    return word.title()


print(int_func('gogi'))
print(int_func('gogi ashot nurik'))
print(int_func('goGi aSHOt NURiK'))


# Решение от преподавателя №1
def int_func(words):
    # function takes words (split by space) and uppercase first letter in any words
    # verify that the all letters its lower latin script and spaces
    for i in words:
        if not ord(i) == 32 and not 97 <= ord(i) <= 122:
            print('Lower latin script and spaces between!\n')
            words = input('Enter words with a space (lower latin script):\n')
            break
        words_list = words.split()
        for i in range(len(words_list)):
            print(words_list[i][0].upper() + words_list[i][1:], end=' ')


int_func(input('Enter words with a space lower latin script:\n'))


# Решение от преподавателя №2
# поменяет только первую букву, остальные оставит прежними
def int_func(word):
    words, result = [], []
    if len(word) > 0:
        for i in word.split():
            words.append(i[0].upper() + i[1:])
        result = ' '.join(words)
    return result


print(int_func(input('Введите строку: ')))


# Решение от преподавателя №3
int_func = lambda sentence: print(sentence.title())

int_func(input('Please enter set of words. '))
