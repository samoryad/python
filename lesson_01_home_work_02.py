time_in_seconds = int(input('введите секунды '))
print(f'время {time_in_seconds // 3600:02}:{time_in_seconds // 60 - time_in_seconds // 3600 * 60:02}:{time_in_seconds % 60:02}')

