'''
Дана строка.
Замените в этой строке все появления буквы `h` на букву `H`, кроме первого и последнего вхождения.
'''

s = str(input('\nПожалуйста, ведите\n\t\t\tстроку\t\u2799\t'))
ch = str(input('символ для замены\t\u2799\t'))
print('\n' + '\u25B5\u25BF' * 15)

a = s.find(ch)                      # Идекс первого вхождения.
x = s[:a + 1]                       # Отсечение первой части строки, от 0 по индекс первого вхождения (не включая).

b = s.rfind(ch)                     # индекс последнего вхождения (поиск справа налево), первый индекс с конца.

z = s[b::]                          # Отсечение третьей части строки, от последнего индекса вхожения (включительно).

y = s[a + 1: b]                     # Отсечение второй, средней части строки, от первого вхождения + 1(не включая),
                                    # по последний индекс вхождения (не включая).

yr = y.replace(ch, ch.upper())      # Замена нижнего регистра на верхний, заданого символа. (Новая строка).

xyz = (x + yr + z)                  # Склеивание первой части строки с изменённой средней и третьей строками.

print('\t' + xyz)                          # Вывод результата.
print('\u25B5\u25BF' * 15)
