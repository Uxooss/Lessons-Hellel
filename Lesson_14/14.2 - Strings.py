"""
Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
Окончанием ввода пусть служит пустая строка.
Каждая введённая строка, в файле, должна начинаться с новой строки.
"""

lst = []

while True:
    s = input()
    if s != '':
        lst.append(s)
    else:
        break


file = open('14.2 - Strings.txt', 'w', encoding='utf-8')

for i in lst:
    file.write(i)
    file.write('\n')

print('\n\t\u27AD\tФайл  "14.2 - Strings.txt"  создан.')

file.close()
