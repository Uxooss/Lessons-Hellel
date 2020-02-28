# Написать функцию is_year_leap, принимающую 1 аргумент — год,
# и возвращающую True, если год високосный, и False иначе.


def is_year_leap(y):
    """
    Функция проверяет высокосный год.

    :param y: Вводимый год
    :return:
    """
    if y % 4 == 0:
        return True
    else:
        return False


print()
y = int(input('Введите год: '))

res = is_year_leap(y)

if res:
    print('\n\t{}'.format(y), 'год - высокосный.')
else:
    print('\n\t{}'.format(y), 'год - не высокосный.')
