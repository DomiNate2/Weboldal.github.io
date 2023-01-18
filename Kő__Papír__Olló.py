import random

szamolas=0
nyeres=0
vesztes=0
dontetlen=0

# meddig fusson le a program
while szamolas < 3:

    # hányszor fusson le a program
    szamolas= szamolas+1

    valasztas = ['kõ', 'papír', 'olló']

    # játékos választása
    jatekosvalasztas = input("Kérlek válassz: kõ, papír, olló: ")

    # számítógép választása
    gepvalasztas = random.choice(valasztas)

    print("Játékos választása:", jatekosvalasztas)
    print("Számítógép választása:", gepvalasztas)

    # nyerés/vesztés/döntetlen logikája
    if jatekosvalasztas == gepvalasztas:
        print("Döntetlen")
        dontetlen=dontetlen+1
    elif jatekosvalasztas == "kõ" and gepvalasztas == "papír":
        print("Elvesztette a kört!")
        vesztes=vesztes+1
    elif jatekosvalasztas == "papír" and gepvalasztas == "olló":
        print("Elvesztette a kört!")
        vesztes=vesztes+1
    elif jatekosvalasztas == "olló" and gepvalasztas == "kõ":
        print("Elvesztette a kört!")
        vesztes=vesztes+1
    else:
        print("Megnyerte a kört!")
        nyeres=nyeres+1


# ki nyerte/veszttte el a játékot
if nyeres > vesztes:
    print("Ön nyerte a játékot! A gép elsírta magát!")
elif dontetlen > nyeres and vesztes:
    print("A játék döntetlen lett! Odakint rendezzék le a nézeteltérésüket!")
else:
    print("Elvesztette a játékot! A gép nyerte meg a játékot!")

print("Ennyi volt a játék mára!")
