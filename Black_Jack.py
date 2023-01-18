import random

# létrehozunk két listát, egyet a gépnek, másikat a játékosnak
gep_kartyak=[]
jatekos_kartyak=[]

# A gépnek nem lehet több kártyája 2-nél
while len(gep_kartyak) != 2:
    gep_kartyak.append(random.randint(1,11))
    # Ha a gépnek a kártyái egyenlõ 2-vel, akkor mgmutassa a gép a káryáit
    if len(gep_kartyak) == 2:
        print("A gepnek ennyi kartyaja van: ", gep_kartyak[1])


# ugyanaz mint az imént, csak most a játékosra nézve
while len(jatekos_kartyak) != 2:
    jatekos_kartyak.append(random.randint(1,11))
    if len(jatekos_kartyak) == 2:
        print("Ennyi kartyad van: ", jatekos_kartyak)

# Ha a gép kártyái elérték a 21-et akkor a gép nyert 
if sum(gep_kartyak) == 21:
    print("A gepnek 21 kartyaja van es nyert! ")
# Ha a gép kértyáinak az összege túllépte az értéket akkor a gép vesztett
elif sum(gep_kartyak) > 21:
    print("A gep besokkalt, tullepte a tetet! ")


while sum(jatekos_kartyak) < 21:
    akcio = input("Megallsz vagy lapot szeretnel huzni: ")
    if akcio == "huzok" or "lapot huzok":
        jatekos_kartyak.append(random.randint(1, 11))
        print("Most van nalad", sum(jatekos_kartyak), "ezekbol a kartyakbol", jatekos_kartyak)
    elif akcio == "megallok" or "allok":
        print("A gepnek osszesen ennyi van ", sum(gep_kartyak), "ebbol", gep_kartyak)
        print("Neked osszesen ennyi van ebbol ", sum(gep_kartyak), "ebbol", gep_kartyak)
        if sum(gep_kartyak) > sum(jatekos_kartyak):
            print("A Gep nyert!")
        else:
            print("Te nyertel! Gratulalok.")
            break

if sum(jatekos_kartyak) > 21:
    print("Elvesztetted a tetet! A gep nyert.")
elif sum(jatekos_kartyak) == 21:
    print("BlackJack-ed van! Gyoztel!")