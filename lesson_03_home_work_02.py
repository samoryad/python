def my_data(**kwargs):
    """ Функция использует на вводе именные аргументы, а выводит строку значений через пробел"""

    a = kwargs
    a_values = a.values()
    print(' '.join(a_values))


my_data(name='Уася', surname='Пупкинс', born_year='2000', town='Москва',
        e_mail='uasya.pupkins@mail.ru', tel='89261234567')


# Решение от преподавателя №1
def personal_info(**kwargs):
    return kwargs


print(personal_info(name=input('Enter your name: '), surname=input('Enter your surname: '),
                    birthday=input('Enter your birthday'), city=input('Enter your city'),
                    email=input('Enter your email'), phone_number=input('Enter your phone number')))


# Решение от преподавателя №2
def person_inf(name, surname, birthday, city, email, phone):
    return f'Name - {name}; Surname - {surname}; birthday - {birthday}; city - {city}; ' \
           f'email - {email}; phone - {phone}'


print(person_inf(name='Alice', surname='Selezneva', birthday='21.09.67', city='Moscow',
                 email='alice.selezneva@mail.ru', phone='143-91-19'))
