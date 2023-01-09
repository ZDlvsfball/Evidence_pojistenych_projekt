from data import *


while True:
    print("------------------------")
    print("Evidence pojištěných")
    print("------------------------")
    print("\n")


    print("Vyberte si akci:")
    print("1 - Přidat nového pojištěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojištěného")
    print("4 - Ukončit")


    vstup =  nacti_cislo("Zadej číslo:\n","Špatná volba!")


    #1.možnost přidání nového pojištěnce
    if vstup == 1:

        pridani_uzivatele()










    #2.možnost výpisu celého seznamu
    if  vstup==2:
        vypis()

    #3.možnost vyhledání pojištěného
    if vstup == 3:
        vyhledavac()



    #4. možnost konec aplikace
    if vstup == 4:

        print("Zvolili jste konec programu, děkujeme za použití.")
        exit()




