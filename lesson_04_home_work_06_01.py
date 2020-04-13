from itertools import count, cycle

for el in count(3):
    if el > 4:
        break
    else:
        c = 0
        for i in cycle(['a', 3, 'b', 4]):
            if c > 2:
                break
            else:
                print(i)
                c += 1


