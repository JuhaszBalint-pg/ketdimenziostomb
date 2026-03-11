tomb = []

sor = 4
oszlop = 3
szam = 1

for i in range(sor):
    sor_tomb = []
    for j in range(oszlop):
        sor_tomb.append(szam)
        szam += 1
    tomb.append(sor_tomb)

print(tomb)