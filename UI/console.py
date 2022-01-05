from Domain.cheltuiala import to_string
from Logic.crud import adauga_cheltuiala, sterge_cheltuiala, modificare_cheltuiala
from Logic.functionalitati import stergere,sume_lunare,descrescator_dupa_suma, cea_mai_mare_dupa_tip,adauga_suma
import datetime

def ui_adauga_cheltuiala(lista):
    numar_apartament = int(input("Introduceti numarul apartamentului."))
    suma = int(input("Introduceti suma."))
    data = datetime.date(int(input("Introduceti anul.")), int(input("Introduceti luna.")),int(input("Introduceti ziua.")))
    tip = input("Introduceti tipul(intretinere, canal, alte cheltuieli)")

    return adauga_cheltuiala(numar_apartament, suma, data, tip, lista)


def ui_sterge_cheltuiala(lista):
    numar_apartament = int(input("introduceti numarul apartamentului cheltuielii care se va sterge: "))

    return sterge_cheltuiala(numar_apartament, lista)

def ui_modifica_cheltuiala(lista):
    numar_apartament_cheltuiala = int(input("Dati numarul apartamentului cheltuielii de modificat."))
    suma = int(input("Dati noua suma sau 0 pentru a nu schimba: "))
    data = datetime.date(int(input("Introduceti anul nou sau 0")), int(input("Introduceti luna noua sau 0")),int(input("Introduceti ziua noua sau 0")))
    tip = input("Dati noul tip (intretinere, canal, alte cheltuieli) sau nimic pt. a nu schimba: ")

    return modificare_cheltuiala(numar_apartament_cheltuiala, suma, data, tip,  lista)

def ui_show_all(lista):
    for i in range(len(lista)):
        print(to_string(lista[i]))

def ui_stergere(lista):
    numar_apartament = int(input("introduceti numarul apartamentului cheltuielilor care se vor sterge: "))

    return stergere(numar_apartament, lista)

def ui_adauga_suma(lista):
    valoare = int(input("Dati valoarea care se va aduna "))
    data = datetime.date(int(input("Introduceti anul")), int(input("Introduceti luna")),int(input("Introduceti ziua")))

    return adauga_suma(valoare, data, lista)

def ui_cea_mai_mare_dupa_tip(lista):
    tip = int(input("Dati tipul "))

    return cea_mai_mare_dupa_tip(tip, lista)

def ui_descrescator_dupa_suma(lista):
    return descrescator_dupa_suma(lista)

def ui_sume_lunare(lista):
    data1 = datetime.date(int(input("Introduceti anul")), int(input("Introduceti luna")),int(input("Introduceti ziua de inceput a lunii")))
    data2 = datetime.date(int(input("Introduceti anul")), int(input("Introduceti luna")),int(input("Introduceti ziua de sfarsit a lunii")))

    return sume_lunare(data1, data2, lista)

def print_options():
    print("1. Adaugare cheltuiala.")
    print("2. Stergere cheltuiala")
    print("3. Modificare cheltuiala")
    print("4. Afiseaza toate cheltuielile")
    print("5. Stergerea tuturor cheltuielilor pt un apartament dat")
    print("6. Adunarea unei valori la toate cheltuielile dintr-o dată citită")
    print("7. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.")
    print("8. Ordonarea cheltuielilor descrescător după sumă")
    print("9. Afișarea sumelor lunare pentru fiecare apartament")
    print("10. Iesire")

def run_menu(lista):
    while True:
        print_options()
        option = int(input("Cititi optiuniea: "))
        if option == 1:
            lista = ui_adauga_cheltuiala(lista)
            print("Cheltuiala adaugata cu succes!")
        elif option == 2:
            lista = ui_sterge_cheltuiala(lista)
            print("Cheltuiala stearsa cu succes!")
        elif option == 3:
            lista = ui_modifica_cheltuiala(lista)
            print("Cheltuiala modificata cu succes!")
        elif option == 4:
            ui_show_all(lista)
        elif option == 5:
            ui_show_all(ui_stergere(lista))
        elif option == 6:
            ui_show_all(ui_adauga_suma(lista))
        elif option == 7:
            ui_cea_mai_mare_dupa_tip(lista)
        elif option == 8:
            ui_show_all(ui_descrescator_dupa_suma(lista))
        elif option == 9:
            ui_show_all(ui_sume_lunare(lista))
        elif option == 10:
            break
        else:
            print("optiune invalida !")
