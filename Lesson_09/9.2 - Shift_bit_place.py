'''
Написать функцию, циклически сдвигающую целое число на N разрядов вправо или влево, в зависимости от третьего
параметра функции. Функция должна принимать три параметра: в первом параметре передаётся число для сдвига, второй
параметр задаёт количество разрядов для сдвига (по умолчанию сдвиг на 1 разряд), 3-й булевский параметр задаёт
направление сдвига (по умолчанию влево (False)).
'''


def bit_shift(num, shft=1, drct=False):
    if not drct:
        num = num * (10 ** -shft)
    elif drct:
        num = num * (10 ** shft)
    return num

# ----------------------------------------
# Без ввода данных:
print()

res = bit_shift(225)
print(res)

res = bit_shift(205, 2, True)
print(res)

# -----------------------------------------
# С ввод данных:

n = int(input('\nInput number:\t'))
qtn = str(input('By default, bit will be shifted left by one digit.\n'
                'Would you like to change value shift and direction? (y / n):\t'))

if qtn == 'y':
    s = int(input('Set shift value:\t'))
    d = str(input('Set shift direction ("-" or "+"):\t'))
elif qtn == 'n':
    s = 1
    d = False

if d == '-':
    d = False
elif d == '+':
    d = True

res = bit_shift(n, s, d)
print(res)
