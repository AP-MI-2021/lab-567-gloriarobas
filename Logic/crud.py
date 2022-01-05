from Domain.cheltuiala import creeaza_cheltuiala, get_numar_apartament, get_suma, get_data, get_tip


def get_by_numar_apartament(lista_cheltuieli, numar_apartament):
    '''
    gaseste o cheltuiala dupa numar_apartament
    :param lista_cheltuieli: lista de obiecte cheltuiala
    :param numar_apartament: un numar intreg
    :return: cheltuiala cu numar_apartament dat sau None daca nu exista
    '''
    for cheltuiala in lista_cheltuieli:
        if get_numar_apartament(cheltuiala) == numar_apartament:
            return cheltuiala
    return None


def adauga_cheltuiala(numar_apartament, suma, data, tip, lista):

    cheltuiala = creeaza_cheltuiala(numar_apartament, suma, data, tip)

    return lista + [cheltuiala]


def sterge_cheltuiala(numar_apartament, lista):
    return [cheltuiala for cheltuiala in lista if get_numar_apartament(cheltuiala) != numar_apartament]


def modificare_cheltuiala(numar_apartament, suma, data, tip, lista):
    lista_modificata = []
    for cheltuiala in lista:
        if get_numar_apartament(cheltuiala) == numar_apartament:
            cheltuiala_noua = creeaza_cheltuiala(
                numar_apartament,
                suma if suma != 0 else get_suma(cheltuiala),
                data if data != "" else get_data(cheltuiala),
                tip if tip != '' else get_tip(cheltuiala),
            )
            lista_modificata.append(cheltuiala_noua)
        else:
            lista_modificata.append(cheltuiala)

    return lista_modificata
