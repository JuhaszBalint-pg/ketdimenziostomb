tabla = [
    ['X', 'O', None],
    [None, 'X', 'O'],
    ['O', None, 'X']
]


for i in range(0, len(tabla)):
    for j in range(0, len(tabla)):
        if tabla [i][j] == None:
            print('_', end = ' ')
        else:
            print(tabla[i][j], end = ' ')
    print()

print(tabla)
tabla[0][2] = 'O'
print()



for i in range(0, len(tabla)):
    for j in range(0, len(tabla)):
        if tabla [i][j] == None:
            print('_', end = ' ')
        else:
            print(tabla[i][j], end = ' ')
    print()

print(tabla)