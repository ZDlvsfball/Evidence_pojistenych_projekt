import pandas as pd
seznam_pojistenych = {
    1:{"jmeno":"Jan","prijmeni":"Novák","vek":34,"telefon": 123456789},
    2:{"jmeno":"Petr","prijmeni":"Johan","vek":56,"telefon": 123356689},
    3:{"jmeno":"Roman","prijmeni":"Cerný","vek":67,"telefon": 111456189},
    4:{"jmeno":"Lukáš","prijmeni":"Hanzlík","vek":23,"telefon": 199453389},

}

def vyhledavac():
    searchingname = input("Zadejte jméno hledané osoby:\n")
    hledane_jmeno = searchingname.lower().capitalize()
    searchingsurname = input("Zadejte přijmení:\n")
    hledane_prijmeni = searchingsurname.lower().capitalize()
    for i in seznam_pojistenych:
        if hledane_jmeno in seznam_pojistenych[i].values():
            print(' '.join(map(str, seznam_pojistenych[i].values())))
        elif hledane_prijmeni and hledane_jmeno in seznam_pojistenych[i].values():
            print(' '.join(map(str,seznam_pojistenych[i].values())))
        elif hledane_jmeno in seznam_pojistenych[i].values() and hledane_prijmeni not in seznam_pojistenych[i].values():
            print(' '.join(map(str,seznam_pojistenych[i].values())))
        elif hledane_prijmeni in seznam_pojistenych[i].values() and hledane_jmeno not in seznam_pojistenych[i].values():
            print(' '.join(map(str,seznam_pojistenych[i].values())))
        else:
            "Bohužel vámi zadané jméno a přijmení neodpovídá žádnému záznamu."


def vypis():

        for id,info in seznam_pojistenych.items():
            print("\nPerson ID:",id)

            for key in info:
                print(key + ':',info[key])








def nacti_cislo(text_zadani, text_chyba):
    spatne = True
    while spatne:
        try:
            cislo = float(input(text_zadani))
            if cislo > 4:
                print(text_chyba)
            spatne = False
        except ValueError:
            print(text_chyba)
        else:
            return cislo

def nacti_vek_a_telefon(text_zadani, text_chyba):
    spatne = True
    while spatne:
        try:
            cislo =int(input(text_zadani))

            spatne = False
        except ValueError:
            print(text_chyba)
        else:
            return cislo


def pridani_uzivatele():
        nove_id = len(seznam_pojistenych) + 1
        # jméno
        jmeno_zad_uzi = input("Zadejte jméno pojištěného:\n")
        nove_jmeno = jmeno_zad_uzi.lower().capitalize()
        # příjmení
        prijmeni_zad_uzi = input("Zadejte přijmení:\n")
        nove_prijmeni = prijmeni_zad_uzi.lower().capitalize()
        # věk
        nove_vek = nacti_vek_a_telefon("Zadejte váš věk:\n","Špatný formát!")
        # telefon
        nove_telefon = nacti_vek_a_telefon("Zadejte vaše telefoní číslo bez + 420:\n", "Špatný formát")
        seznam_pojistenych.update(
            {nove_id: {"jmeno": nove_jmeno, "prijmeni": nove_prijmeni, "vek": nove_vek, "telefon": nove_telefon}})
        print("Data byla uložena, děkujeme.")
