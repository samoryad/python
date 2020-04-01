with open('text_file_for_hw_02.txt', 'r', encoding='utf-8') as my_file:

    content = my_file.readlines()
    print(f'Всего строк: {len(content)}')
    counter = 1
    for line in content:
        print(f'Кол-во слов в строке {counter} равно: {line.count(" ") + 1}')
        counter += 1
    print(content)
