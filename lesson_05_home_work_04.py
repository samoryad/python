with open('text_file_for_hw_04.txt', 'r', encoding='utf-8') as my_file:
    russian_list = ['Один', 'Два', 'Три', 'Четыре']
    new_list = []
    counter = 0
    for line in my_file:
        el = line.split()
        el[0] = russian_list[counter]
        result = ' '.join(el)
        counter += 1
        new_list.append(result + '\n')
        # решение через добавление строки
        # with open('text_file_for_hw_04_01.txt', 'a', encoding='utf-8') as new_file:
        #     new_file.write(f'{result}\n')
        with open('text_file_for_hw_04_01.txt', 'w', encoding='utf-8') as new_file:
            new_file.writelines(new_list)
