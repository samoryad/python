first_distance = int(input('введите, сколько спортсмен пробежал за первый день: '))
final_distance = int(input('введите, сколько ему нужно пробежать всего: '))
days = 1
if final_distance > 0 and first_distance > 0:
    while first_distance < final_distance:
        first_distance += first_distance * 0.1
        days += 1
        print(days, 'день -', '%.2f' % first_distance)
    print(f' на {days}-й день спортсмен достиг результата {final_distance}')
else:
    print('введена некорректная дистанция')

