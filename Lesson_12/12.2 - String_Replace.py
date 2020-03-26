"""
меется строка вида: AABABBAABBBAB. Необходимо написать функцию которая заменит буквы A на B, а B,
соответственно, на A. Замену можно производить ТОЛЬКО используя функцию replace().
В результате применения функции к исходной строке, функция должна вернуть строку: BBABAABBAAABA
"""


def string_replace(s):
    s1 = ''
    i = 0

    while i != len(s):
        if s[i] == 'A':
            s1 = s1 + s[i].replace('A', 'B')
        elif s[i] == 'B':
            s1 = s1 + s[i].replace('B', 'A')
        else:
            s1 = s1 + s[i]
        i += 1
    return s1


print(string_replace('AABABBAABBBAB'))
