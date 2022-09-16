# 4. Задана натуральная степень n. Сформировать случайным образом список
# коэффициентов(значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# *Пример: *

# -n = 2 = > 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def random_koef(n):
    koef_list = []
    for i in range(0, n+1):
        koef_list.append(random.randint(0, 100))
        if i == 0:
            while koef_list[0] == 0:
                del koef_list[0]
                koef_list.append(random.randint(0, 100))
    return koef_list


def gen_polinom2(n):
    list_x = []
    while n > 0:
        if n == 1:
            list_x.append(f'x')
        else:
            list_x.append(f'x^{n}')
        n -= 1
    list_x.append('')
    return list_x


def number_input(input_string):
    '''
    Функция для проверки ввода числа.
    '''
    while type:
        digit = input(input_string)
        try:
            digit = int(digit)
            return digit
        except ValueError:
            print("Введено неверное значение. Только числа!!!")


n = number_input('введите степень полинома: ')
ran_lst = random_koef(n)
koef_list = gen_polinom2(n)
print(ran_lst)
list_koef = list(koef_list)
list_res = list(zip(list_koef, ran_lst))


print(gen_polinom2(n))

print(list_res)

# kor_res = tuple(list_res)
# print(kor_res)

# list_res1 = []
# for i in range(len(list_res)):
#     list_res1 += list_res[i]
#     if i % 2 == 0:
#         print(f'{list_res1[i]} * ')
#     elif i % 2 != 0:
#         print(f'{list_res1[i]} + ')
# print('= 0')


# print(list_res1)
