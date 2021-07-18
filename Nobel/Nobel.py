#Osztály az adatok beolvasásához
class Adatok:
    def __init__(self, sor):
        split= sor.split(';')
        self.Evszam =int(split[0])
        self.Tipus =split[1]
        self.Keresztnev =split[2]
        self.Vezeteknev =split[3]

#Adatok beolvasása 
with open("nobel.csv","r", encoding="utf-8") as Beolvas:
    fejlec = Beolvas.readline()
    lista = [Adatok(x.strip()) for x in Beolvas]

#3. feladat: 
print(f"3. feladat: {[x.Tipus for x in lista if x.Keresztnev == 'Arthur B.' and x.Vezeteknev == 'McDonald'][0]}")

#4. feladat:
print(f"4. feladat: {[x.Keresztnev + ' ' + x.Vezeteknev for x in lista if x.Tipus == 'irodalmi' and x.Evszam == 2017][0]}")

#5. feladat: 
print("5. feladat:")
[print(f"\t{x.Evszam}: {x.Keresztnev}") for x in lista if x.Evszam>1990 and x.Vezeteknev=="" and x.Tipus=="béke"]

#6. feladat:
print("6. feladat: ")
[print(f"\t{x.Evszam}: {x.Keresztnev} {x.Vezeteknev}({x.Tipus})") for x in lista if x.Vezeteknev.__contains__('Curie')]


#7. feladat
print("7. feladat: ")
tipusok = {x.Tipus for x in lista}
valogatott = dict()
for x in tipusok:
    for y in lista:
        if x==y.Tipus:
            valogatott[x]=valogatott.get(x, 0)+1
for x,y in valogatott.items():
    print(f"\t{x:<27}{y:>4} db")

#8. feladat:
print("8. feladat: orvosi.txt")
with open("orvosi.txt","w", encoding="utf-8") as Kiiras:
    [Kiiras.write(f"{x.Evszam}:{x.Keresztnev} {x.Vezeteknev}\n") for x in sorted(lista, key=lambda y: y.Evszam) if x.Tipus=="orvosi"]
    
