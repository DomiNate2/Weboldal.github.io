import random

szamolas=0
nyeres=0
vesztes=0
dontetlen=0

# meddig fusson le a program
while szamolas < 3:

    # h�nyszor fusson le a program
    szamolas= szamolas+1

    valasztas = ['k�', 'pap�r', 'oll�']

    # j�t�kos v�laszt�sa
    jatekosvalasztas = input("K�rlek v�lassz: k�, pap�r, oll�: ")

    # sz�m�t�g�p v�laszt�sa
    gepvalasztas = random.choice(valasztas)

    print("J�t�kos v�laszt�sa:", jatekosvalasztas)
    print("Sz�m�t�g�p v�laszt�sa:", gepvalasztas)

    # nyer�s/veszt�s/d�ntetlen logik�ja
    if jatekosvalasztas == gepvalasztas:
        print("D�ntetlen")
        dontetlen=dontetlen+1
    elif jatekosvalasztas == "k�" and gepvalasztas == "pap�r":
        print("Elvesztette a k�rt!")
        vesztes=vesztes+1
    elif jatekosvalasztas == "pap�r" and gepvalasztas == "oll�":
        print("Elvesztette a k�rt!")
        vesztes=vesztes+1
    elif jatekosvalasztas == "oll�" and gepvalasztas == "k�":
        print("Elvesztette a k�rt!")
        vesztes=vesztes+1
    else:
        print("Megnyerte a k�rt!")
        nyeres=nyeres+1


# ki nyerte/veszttte el a j�t�kot
if nyeres > vesztes:
    print("�n nyerte a j�t�kot! A g�p els�rta mag�t!")
elif dontetlen > nyeres and vesztes:
    print("A j�t�k d�ntetlen lett! Odakint rendezz�k le a n�zetelt�r�s�ket!")
else:
    print("Elvesztette a j�t�kot! A g�p nyerte meg a j�t�kot!")

print("Ennyi volt a j�t�k m�ra!")
