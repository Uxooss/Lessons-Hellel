# Дан список чисел. Определите, сколько в нем встречается различных чисел.
#     - Примечание. Эту задачу на Питоне можно решить в одну строчку.

a = input('\nВведите список чисел:\t').split()
print('\nВ введённом списке чисел ', len(set(a)), ' уникальных')

