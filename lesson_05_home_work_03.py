with open('text_file_for_hw_03.txt', 'r', encoding='utf-8') as my_file:
    total = 0
    counter = 0
    for line in my_file:
        counter += 1
        el = line.split()
        salary = float(el[-1])
        total += salary
        if salary < 20000:
            print(line)
    print(f'Средняя зарплата всех сотрудников: {round(total / counter, 2)}')

with open('text_file_for_hw_03_01.txt', 'w', encoding='utf-8') as print_file:
    print(f'Средняя зарплата всех сотрудников: {round(total / counter, 2)}', file=print_file)
