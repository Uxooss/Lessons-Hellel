# Напишите программу, которая считывает целое число и выводит текст:
# Первая строка содержит следующее значение, а втора строка содержит предыдущее значение введёного числа

a = int(input('\nPlease enter an integer number: '))
print('The next number for the number', str(a), 'is', (a + 1), '\b.')
print('The previous number for the number', str(a), 'is', (a - 1), '\b.')
