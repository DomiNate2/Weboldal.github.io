import random

# újradobás értékhez rendelés
ujradobas="igen"
# változók deklarálása
psz=0
gsz=0
ossz=0

# amíg újradobás egyenlő igennel addig lefut a program
while ujradobas == "igen" or ujradobas == "IGEN" or "Igen":
    # megkérdezzük a felhasználóttól, hogy dobókockával szeretne játszani
    ksz=int(input("Hany kockaval szeretne jatszani (1-5): "))
    if ksz == 1:
          # a két dobókocka értékének a megadása 1-6-ig 
          kocka1=random.randint(1,6)
          kocka2=random.randint(1,6)

          # itt rakhat tétet, ha szeretne 
          tetel=int(input("Mennyit szeretne felrakni a jatekra: "))

          # összeadja a kockák értékeit 
          ossz=kocka1+kocka2
          # kiszámolja a dobások átlagát
          atlag=kocka1/ossz
           
          # kiiratások
          print("Az ertekek: ")
          print("Az elso dobas =", kocka1, "\nA masodik dobas =", kocka2)
          print("A pontszamok: \nEn pontszamom: ",kocka1, ",", "Gep pontszama: ", kocka2)
          print("\nAtlag: ", atlag)

          # ki nyert/veszített
          if kocka1 == kocka2:
            print("Az ertekek megegyeznek!")
          elif kocka1>kocka2:
            print("On nyerte a jatekot! On nyert ennyi osszeget: ", tetel)
          else:
            print("A gep nyerte a jatekot! On elvesztett ennyit: ", tetel)

          # megkérdezzi a felhasználótól, hogy újraszeretne-e játszani
          ujradobas=input("\nUjraszeretne jatszani: ")
    
    elif ksz == 2:
        kocka1=random.randint(1,6)
        kocka2=random.randint(1,6)
        kocka3=random.randint(1,6)
        kocka4=random.randint(1,6)

        psz=kocka1+kocka2
        gsz=kocka3+kocka4

        ossz=kocka1+kocka2+kocka3+kocka4
        atlag=psz/ossz

        tetel=int(input("Mennyit szeretne felrakni a jatekra: "))

        print("Az ertekek: ")
        print("Az elso dobas =", kocka1, "A masodik dobas=", kocka2, "\nA harmadik dobas =", kocka3, "A negyedik dobas =", kocka4)
        print("A pontszamok: \nEn pontszamom: ",psz, ",", "Gep pontszama: ", gsz)
        print("\nAz atlag: ", atlag)

        if kocka1 and kocka2 == kocka3 and kocka4:
            print("Az ertekek megegyeznek!")
        elif kocka1 and kocka2>kocka3 and kocka4:
            print("On nyerte a jatekot! On nyert ennyi osszeget: ", tetel)
        else:
            print("A gep nyerte a jatekot! On elvesztett ennyi osszeget: ", tetel)

        ujradobas=input("\nUjraszeretne jatszani: ")

    elif ksz == 3:
        kocka1=random.randint(1,6)
        kocka2=random.randint(1,6)
        kocka3=random.randint(1,6)
        kocka4=random.randint(1,6)
        kocka5=random.randint(1,6)
        kocka6=random.randint(1,6)

        psz=kocka1+kocka2+kocka3
        gsz=kocka4+kocka5+kocka6

        ossz=kocka1+kocka2+kocka3+kocka4+kocka5+kocka6
        atlag=psz/ossz

        tetel=int(input("Mennyit szeretne felrakni a jatekra: "))

        print("Az ertekek: ")
        print("Az elso dobas =", kocka1, "A masodik dobas =", kocka2, "A harmadik dobas =", kocka3, "\nA negyedik dobas =", kocka4, "Az otodik dobas =", kocka5, "A hatodik dobas =", kocka6)
        print("A pontszamok: \nEn pontszamom: ",psz, ",", "Gep pontszama: ", gsz)
        print("\nAz atlag: ", atlag)

        if kocka1 and kocka2 and kocka3 == kocka4 and kocka5 and kocka6:
            print("Az ertekek megegyeznek!")
        elif kocka1 and kocka2 and kocka3>kocka4 and kocka5 and kocka6:
            print("On nyerte a jatekot! On nyert ennyi osszeget :", tetel)
        else:
            print("A gep nyerte a jatekot! On elvesztett ennyi osszeget: ", tetel)

        ujradobas=input("\nUjraszeretne jatszani: ")

    elif ksz == 4:
        kocka1=random.randint(1,6)
        kocka2=random.randint(1,6)
        kocka3=random.randint(1,6)
        kocka4=random.randint(1,6)
        kocka5=random.randint(1,6)
        kocka6=random.randint(1,6)
        kocka7=random.randint(1,6)
        kocka8=random.randint(1,6)

        psz=kocka1+kocka2+kocka3+kocka4
        gsz=kocka5+kocka6+kocka7+kocka8

        ossz=kocka1+kocka2+kocka3+kocka4+kocka5+kocka6+kocka7+kocka8
        atlag=psz/ossz

        tetel=int(input("Mennyit szeretne felrakni a jatekra: "))

        print("Az ertekek: ")
        print("Az elso dobas =", kocka1, "A masodik dobas =", kocka2, "A harmadik dobas =", kocka3, "A negyedik dobas = ", kocka4, "\nAz otodik dobas =", kocka5, "A hatodik dobas =", kocka6, "A hetedik dobas =", kocka7, "A nyolcadik dobas =", kocka8)
        print("A pontszamok: \nEn pontszamom: ",psz, ",", "Gep pontszama: ", gsz)
        print("\nAz atlag: ", atlag)

        if kocka1 and kocka2 and kocka3 and kocka4 == kocka5 and kocka6 and kocka7 and kocka8:
            print("Az ertekek megegyeznek!")
        elif kocka1 and kocka2 and kocka3 and kocka4 > kocka5 and kocka6 and kocka7 and kocka8:
            print("On nyerte a jatekot! On nyert ennyi osszeget", tetel)
        else:
            print("A gep nyerte a jatekot!On vesztett ennyi osszeget: ", tetel)

        ujradobas=input("\nUjraszeretne jatszani: ")

    elif ksz == 5:
        kocka1=random.randint(1,6)
        kocka2=random.randint(1,6)
        kocka3=random.randint(1,6)
        kocka4=random.randint(1,6)
        kocka5=random.randint(1,6)
        kocka6=random.randint(1,6)
        kocka7=random.randint(1,6)
        kocka8=random.randint(1,6)
        kocka9=random.randint(1,6)
        kocka10=random.randint(1,6)

        psz=kocka1+kocka2+kocka3+kocka4+kocka5
        gsz=kocka6+kocka7+kocka8+kocka9+kocka10

        ossz=kocka1+kocka2+kocka3+kocka4+kocka5+kocka6+kocka7+kocka8+kocka9+kocka10
        atlag=psz/ossz

        tetel=int(input("Mennyit szeretne felrakni a jatekra: "))

        print("Az ertekek: ")
        print("Az elso dobas =", kocka1, "A masodik dobas =", kocka2, "A harmadik dobas =", kocka3, "A negyedik dobas = ", kocka4, "Az otodik dobas =", kocka5, "\nA hatodik dobas =", kocka6, "A hetedik dobas =", kocka7, "A nyolcadik dobas =", kocka8, "A kilencedik dobas =", kocka9, "A tizedik dobas =", kocka10)
        print("A pontszamok: \nEn pontszamom: ",psz, ",", "Gep pontszama: ", gsz)
        print("\nAz atlag: ", atlag)

        if kocka1 and kocka2 and kocka3 and kocka4 and kocka5 == kocka6 and kocka7 and kocka8 and kocka9 and kocka10:
            print("Az ertekek megegyeznek!")
        elif kocka1 and kocka2 and kocka3 and kocka4 and kocka5 > kocka6 and kocka7 and kocka8 and kocka9 and kocka10:
            print("On nyerte a jatekot! On nyert ennyi osszeget", tetel)
        else:
            print("A gep nyerte a jatekot! On elvesztett ennyi osszeget: ", tetel)

        ujradobas=input("\nUjraszeretne jatszani: ")

    # Ha rossz opciót ad meg a felhasználó
    else:
        print("Nincs ilyen opcio!")


