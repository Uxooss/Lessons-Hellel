'''
Дана строка.
Замените в этой строке все появления буквы `h` на букву `H`, кроме первого и последнего вхождения.
'''

s = str(input('\nПожалуйста, ведите\n\t\t\tстроку\t\u2799\t'))
ch = str(input('символ для замены\t\u2799\t'))
print('\n' + '\u25B5\u25BF' * 20)

i = 0                           # индекс входа
x = 0                           # искомый индекс
cnt = 0
mx = x
mn = x

while x != -1:
    x = (s.find(ch, i))

    if x == -1:
        continue

    i = x + 1
    cnt += 1

ss = s.replace(ch, ch.upper(), cnt - 1)

print(ss)
