# Дано целое, положительное, трёхзначное число.
# Необходимо его перевернуть.
# Например, если ввели число 123, то должно получиться на выходе ЧИСЛО 321.
# ВАЖНО! Работать только с числами. Строки использовать НЕЛЬЗЯ!

x = int(input('\nВведите целое, положительное, трёхзначное число:\t'))
i = '\n\t\tЧисло {} наоборот, будет число {}.\n'

a = (x % 10)
b = (x // 10) % 10
c = (x // 100) % 10

d = ((a * 100) + (b * 10) + c)

print('-' * 56, i.format(x, d), '.' * 54)