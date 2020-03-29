debit = int(input('введите выручку фирмы: '))
credit = int(input('введите издержки фирмы: '))

if debit > credit:
    print('прибыль больше издержек')
    rent = debit / credit * 100
    print('%.2f - рентабельность' % rent)
    employees = int(input('введите количество сотрудников: '))
    print('%.2f - прибыль фирмы на 1 сотрудника' % ((debit - credit) / employees))
elif debit < credit:
    print('компания в убытке')
else:
    print('компания отработала в 0')


