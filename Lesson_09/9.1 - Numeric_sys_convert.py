'''
Написать функцию для перевода десятичного числа в другую систему исчисления (2-36).
Небольшая подсказка. В этой задаче вам понадобится:
    - список
    - метод `revers()` (или срез [::-1], или вместо `revers()` использовать `insert()` тогда не
        придётся разворачивать список), чтоб развернуть список, метод `join()`
    - строка `ascii_uppercase` из модуля `string` (её можно получить если сделать импорт
        `from string import ascii_uppercase`), она содержит все буквы латинского алфавита.
'''

from string import ascii_uppercase


def digit_2_letter(val):
    if val > 9:                             # цифры от 0 до 9, остаются цифрами
        return ascii_uppercase[val-10]      # цифры от 10 и далее, переводятся в буквы (А=11, В=12 и т.д.)
    else:
        return str(val)                     # ф-ия возвращает полученный символ.


def num_convert(num, x):
    val_lst = []
    res = ''

    if num == 0:
        val_lst.append(num)

    while num > 0:
        val_lst.append(num % x)
        num = num // x
    rev_lst = val_lst[::-1]

    for x in rev_lst:
        res = res + digit_2_letter(x)
    return res


num = int(input('\nPlease enter the value:\t\t'))
x = int(input('Please enter the numeral system:\t'))

print(num_convert(num, x))
