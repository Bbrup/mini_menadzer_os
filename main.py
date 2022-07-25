import os
import os.path
from os import path

def lokalizacja():
 os.system('clear')
 print("Jestes w:" + os.getcwd() + "\n")


def menu():
 print('''
 Wybierz Dostepne opcje:
 1.Pokaz lokalizacje
 2.Zmien lokalizacje
 3.Pokaz pliki w obecnej lokalizacji
 4.Pokaz cale drzewo z obecnej lokalizacji
 5.Utworz katalog
 6.Usun katalog
 7.Zmien nazwe
 8.Sprawdz czy plik znajduje sie w obecnej lokalizacji
 9.Koniec
 ''')


while True:
    os.system('clear')
    print("Witaj w Mini Menedżerze")
    menu()

    odp=input()

    if odp == "1":
        os.system('clear')
        lokalizacja()


    if odp=="2":
        lokalizacja()
        print("1.Wedlug sciezki")
        print("2.Cofnij lokalizacje")
        odp_sub = input("\nWybierz dostepna opcje, powrot - dowolny klawisz\n")
        if odp_sub == "1":
             lokalizacja()
             saved_path = os.getcwd()
             odp_sub_sub = input("Podaj sciezke:")
             try:
                  os.chdir(odp_sub_sub)
             except:
                  print("Zostala podana bledna lokalizacja")



        if odp_sub == "2":
            os.system('clear')
            os.chdir('..')
            print("Jestes w:" + os.getcwd() + "\n")


    if odp == "3":
        os.system('clear')
        print(os.listdir())

    if odp == "4":
        for dirpath, dirnames, filenames in os.walk(os.getcwd()):
            print("W lokalizacji: ", dirpath)
            print("Foldery: ", dirnames)
            print("Pliki", filenames)


    if odp == "5":
        os.system('clear')
        odp_sub_sub=input("Podaj nazwe\n")
        try:
         os.mkdir(odp_sub_sub)
         print("Utworzono katalog poprawnie")
        except:
         print("Niepoprawna nazwa")


    if odp == "6":
        os.system('clear')
        print(os.listdir())
        odp_sub = input("Podaj nazwe\n")
        try:
         os.rmdir(odp_sub)
         print("Usunieto poprawnie")
        except:
         print("Niepoprawna nazwa")

    if odp == "7":
        os.system('clear')
        lokalizacja()
        print("Lista plikow: ")
        print(os.listdir())
        odp_sub = input("Podaj ktory folder lub plik zmienic\n")
        odp_rename= input("Podaj na jaka nazwe\n")
        try:
            os.rename(odp_sub,odp_rename)
            print("Poprawnie zmieniono")
        except:
            print("Niepoprawna nazwa")

    if odp == "8":
        os.system('clear')
        x=input("Podaj nazwe pliku do przeszukania: ")
        if path.exists(x)==True:
         print("Plik znajduje sie w lokalizacji")
        else:
         print("Plik nie znajduje sie w lokalizacji")

    if odp == "9":
        break
    input("Kontynuuj...")
