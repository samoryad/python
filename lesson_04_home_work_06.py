from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

count = 0
for el in cycle(['a', 3, 'b', 4]):
    if count > 2:
        break
    else:
        print(el)
        count += 1
