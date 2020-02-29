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


y = int(input('\nВведите год: '))
res = is_year_leap(y)
if res:
    print('\n\t{} год - высокосный.'.format(y))
else:
    print('\n\t{} год - не высокосный.'.format(y))
