rows = int(input('\nВведите высоту фигуры:\t'))
print()
cols = (rows * 2) - 1

# ---------------------------------------------

print(' "A"')

for i in range(rows):
    for j in range(cols):
        if j == rows - 1 - i or j == rows - 1 + i or i == rows - 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()

# ---------------------------------------------

print(' "B"')

for i in range(rows):
    for j in range(cols):
        if rows - 1 - i <= j <= rows - 1 + i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()

# ---------------------------------------------

print(' "C"')

for i in range(rows // 2):
    for j in range(cols // 2):
        if (rows // 2) - 1 - i <= j <= (rows // 2) - 1 + i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
for i in range(rows // 2):
    if i == 0:
        continue
    for j in range(cols // 2):
        if i == j or i == (cols // 2) - j - 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()

# ---------------------------------------------

print(' "D"')

for i in range(rows // 2):
    for j in range(cols // 2):
        if (rows // 2) - 1 - i <= j <= (rows // 2) - 1 + i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
for i in range(rows // 2):
    if i == 0:
        continue
    for j in range(cols // 2):
        if i == j or i == (cols // 2) - j - 1 or j == (cols // 4):
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()
