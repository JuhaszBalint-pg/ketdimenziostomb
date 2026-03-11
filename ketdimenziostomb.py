matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#print(matrix[0][0])

#kiírás
for sor in matrix:
    for oszlop in sor:
        print(oszlop, end =' ')
    print()

#keresés
for i in range(0, len(matrix)):
    for j in range(0, len(matrix)):
        print (matrix [i] [j], end = ' ')
    print()