from collections import namedtuple

def AtszamolPercre(ora,perc):
    return ora * 60 + perc

adas = namedtuple("adas", "Ora Perc AdasDB Nev")

soforok = set()

adasok = []
with open("cb.txt") as f:
    next(f)
    for sor in f:
        a = adas(int(sor.split(';')[0]), int(sor.split(';')[1]), int(sor.split(';')[2]), sor.split(';')[3])
        adasok.append(a)
van4=False
for adas in adasok:
    if adas.AdasDB == 4:
        van4 = True

if van4:
    print("Volt 4 adást indító sofőr")
else:
    print("Nem volt 4 adást indító sofőr")

for adas in adasok:
    soforok.add(adas.Nev)

sofor = input("Kérek egy nevet: ")
if  sofor in soforok:
    hivas_DB = 0
    for adas in adasok:
        if adas.Nev== sofor:
            hivas_DB+=adas.AdasDB
    print(f"{sofor} sofőrnek {hivas_DB} db hívása volt összesen.")
else:
    print("Nincs ilyen nevű sofőr")

with open("cb2.txt", "w") as f:
    f.write("Kezdes;Nev;AdasDB\n")
    for adas in adasok:
        f.write(f"{AtszamolPercre(adas.Ora,adas.Perc)};{adas.Nev};{adas.AdasDB}\n")
