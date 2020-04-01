with open('text_file_for_hw_07.txt', 'r', encoding='utf-8') as my_file:
    counter_01 = 0
    counter_02 = 0
    total = 0
    my_list = []
    my_dict_01 = {}
    for line in my_file:
        content = line.split()
        if int(content[-1]) < int(content[-2]):
            my_list.append(int(content[-2]) - int(content[-1]))
            # print(f'Прибыль компании {content[0]} равна: {my_list[counter]}')
            total += my_list[counter_01 + counter_02]
            counter_01 += 1
        else:
            my_list.append(int(content[-2]) - int(content[-1]))
            counter_02 += 1
        my_dict_01.update({content[0]: my_list[counter_01 + counter_02 - 1]})
        # print(my_dict_01)
    # print(my_list)
    middle = total / counter_01
    # print(f'Средняя прибыль прибыльных компаний равна: {middle}')
    my_dict_02 = {'average_profit': middle}
    # print(my_dict_02)
    my_list_total = [my_dict_01, my_dict_02]
    print(my_list_total)

import json

with open('my_file.json', 'w', encoding='utf-8') as write_f:
    json.dump(my_list_total, write_f, ensure_ascii=False, indent=4)
