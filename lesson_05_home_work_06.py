with open('text_file_for_hw_06.txt', 'r', encoding='utf-8') as my_file:
    new_dict = {}
    for line in my_file:
        # print(line)
        my_dict = {line[:line.index(':')]: line[line.index(' '):]}
        my_str = ''
        my_list = []
        for value in my_dict.values():
            # print(value)
            for el in value:
                if el.isdigit():
                    my_str += el
                elif my_str != '':
                    my_list.append(int(my_str))
                    my_str = ''
            # print(my_str)
            # print(my_list)
            new_dict.update({line[:line.index(':')]: sum(my_list)})
    print(new_dict)
