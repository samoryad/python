my_list = ['a', 20, 24.5, True, (23, 5, True), [1, 'word'], {1, 34, 'word'}, {1: 'a', 2: 'b'}]
print(my_list)
for el in my_list:
    print(type(el))

# решение преподавателя №1
my_list = [(-1 + 0j), 1, 2.2, True, None, 'String', [3, 4], (5, 6, 6.5), {7: 'seven', 8: 'eight'}, {9, 10}, frozenset(),
           range(11), b'twelve', bytearray(b'thirteen'), zip(*[(14, 15), (16, 17), ('a', 'b')]), TypeError]
for i, item in enumerate(my_list):
    print(f'{i}) {item} - {type(item)}')
