def MenuWypisz():
    print("MENU")
    print("1.Pokaz Przedmioty")
    print("2.Dodaj Przedmioty")
    print("3.Użyj Przedmioty")
    print("4.Sprawdz Przedmiot")
    print("5.Wyjdz")

def LiczWage(ekwipunek, wagi):
    calaWaga = 0
    for przedmiot, ilosc in ekwipunek.items():
        calaWaga = calaWaga + ilosc * wagi[przedmiot]
    return(round(calaWaga, 2))

def pokazPrzedmioty(ekwipunek, wagi, maxWaga):
    for przedmiot, ilosc in ekwipunek.items():
        print(f"Przedmiot: {przedmiot}, Ilość: {ilosc}, Waga: {wagi[przedmiot]}")
    print(f"Waga ekwipunku: {LiczWage(ekwipunek, wagi)}/{maxWaga}")

def PlusPrzedmiot(ekwipunek, wagi, maxWaga):
    wyborPrzedmiot = input("podaj przedmiot do dodania: ")
    cena = int(input("podaj cene w zlocie: "))
    calkowicieNowy = True
    for przedmiot, ilosc in ekwipunek.items():
        if wyborPrzedmiot == przedmiot:
            calkowicieNowy = False
    if calkowicieNowy:
        waga = float(input("podaj wage przedmiotu: "))
    else:
        waga = wagi[wyborPrzedmiot]
    zloto = 0
    for przedmiot, ilosc in ekwipunek.items():
        if przedmiot == "zloto":
            zloto = ilosc
    if cena > zloto:
        print(f"Nie masz tyle zlota, masz tylko {zloto}")
        return(ekwipunek)
    nowaWaga = round(LiczWage(ekwipunek, wagi) + waga - cena * wagi["zloto"], 2)
    if nowaWaga > maxWaga:
        print(f"Za ciezko! Waga bylaby {nowaWaga}, a maksymalna to {maxWaga}")
        return(ekwipunek)
    ekwipunek["zloto"] = zloto - cena
    if calkowicieNowy:
        ekwipunek[wyborPrzedmiot] = 1
        wagi[wyborPrzedmiot] = waga
    else:
        ekwipunek[wyborPrzedmiot] = ekwipunek[wyborPrzedmiot] + 1
    return(ekwipunek)

def MinusPrzedmiot(ekwipunek, wagi, maxWaga):
    wyborPrzedmiot = input("podaj przedmiot do usuniencia: ")
    sprzedane = False
    for przedmiot, ilosc in ekwipunek.items():
            if wyborPrzedmiot == przedmiot:
                cena = int(input("podaj cene sprzedazy w zlocie: "))
                nowaWaga = round(LiczWage(ekwipunek, wagi) - wagi[wyborPrzedmiot] + cena * wagi["zloto"], 2)
                if nowaWaga > maxWaga:
                    print(f"Za ciezko! Waga bylaby {nowaWaga}, a maksymalna to {maxWaga}")
                    break
                if (ilosc-1) == 0:
                    del ekwipunek[wyborPrzedmiot]
                else:
                    ekwipunek[wyborPrzedmiot] = ilosc - 1
                sprzedane = True
                break
    if sprzedane:
        zloto = 0
        for przedmiot, ilosc in ekwipunek.items():
            if przedmiot == "zloto":
                zloto = ilosc
        ekwipunek["zloto"] = zloto + cena
        print(f"Sprzedano {wyborPrzedmiot} za {cena} zlota")
    return(ekwipunek)

def Obecnosc(ekwipunek, wagi):
    czyJest = False
    wyborPrzedmiot = input("podaj przedmiot do sprawdzenia: ")
    for przedmiot, ilosc in ekwipunek.items():
        if wyborPrzedmiot == przedmiot:
            print(f"Jest Przedmiot: {przedmiot}, Ilość: {ilosc}, Waga: {wagi[przedmiot]}")
            czyJest = True
    if czyJest == False:
        print(f"Nie ma {wyborPrzedmiot}")

def gra():
    ekwipunek = {"miecz": 1, "mikstura": 3, "zloto": 50}
    wagi = {"miecz": 5, "mikstura": 0.5, "zloto": 0.1}
    maxWaga = 30
    trwa = True
    while trwa:
        MenuWypisz()
        wyborMenu = int(input("podaj wybor: "))
        if wyborMenu == 1:
            pokazPrzedmioty(ekwipunek, wagi, maxWaga)
        elif wyborMenu == 2:
            ekwipunek = PlusPrzedmiot(ekwipunek, wagi, maxWaga)
        elif wyborMenu == 3:
            ekwipunek = MinusPrzedmiot(ekwipunek, wagi, maxWaga)
        elif wyborMenu == 4:
            Obecnosc(ekwipunek, wagi)
        elif wyborMenu == 5:
            trwa = False
gra()
