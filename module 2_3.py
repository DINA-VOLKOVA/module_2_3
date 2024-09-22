my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]  # исходные данные
count = 0   # начальное значение
print('Список', my_list, '\nПоложительные числа из списка')

while count < len(my_list):
    num = my_list[count]    # задаём число из списка
    count = count + 1   # запускаем счетчик
    if num == 0:
        continue    # пропускаем 0
    elif num < 0:
        break
    elif count == len(my_list):
        print(num)
        print('Список закончился')
    else:
        print(num)






