from Domain.cheltuiala import get_numar_apartament, get_suma, get_data, get_tip, creeaza_cheltuiala
from Logic.crud import adauga_cheltuiala, sterge_cheltuiala, get_by_numar_apartament, modificare_cheltuiala


def test_adauga_cheltuiala():
    lista = []
    lista = adauga_cheltuiala(1, 123, '2020-12-12', 'intretinere', lista)
    assert get_numar_apartament(lista[0]) == 1
    assert get_suma(lista[0]) == 123
    assert get_data(lista[0]) == '2020-12-12'
    assert get_tip(lista[0]) == 'intretinere'


def test_sterge_cheltuiala():
    cheltuiala1 = creeaza_cheltuiala(1, 123, '2020-12-12', 'intretinere')
    cheltuiala2 = creeaza_cheltuiala(2, 145, '2020-11-14', 'alte cheltuieli')

    lista = [cheltuiala1, cheltuiala2]
    lista = sterge_cheltuiala(2, lista)

    assert len(lista) == 1
    assert get_by_numar_apartament(lista, 1) == cheltuiala1
    assert get_by_numar_apartament(lista, 2) == None

    lista = [cheltuiala1, cheltuiala2]
    lista2 = sterge_cheltuiala(3, lista)

    assert len(lista2) == 2
    assert get_by_numar_apartament(lista, 1) == cheltuiala1
    assert get_by_numar_apartament(lista, 2) == cheltuiala2


def test_modifica_cheltuiala():
    cheltuiala1 = creeaza_cheltuiala(1, 123, '2020-12-12', 'intretinere')
    cheltuiala2 = creeaza_cheltuiala(2, 145, '2020-11-14', 'alte cheltuieli')

    lista = [cheltuiala1, cheltuiala2]

    lista = modificare_cheltuiala(1, 743, '', '', lista)

    cheltuiala_updatata = get_by_numar_apartament(lista, 1)
    assert get_numar_apartament(cheltuiala_updatata) == 1
    assert get_suma(cheltuiala_updatata) == 743
    assert get_data(cheltuiala_updatata) == '2020-12-12'
    assert get_tip(cheltuiala_updatata) == 'intretinere'


    assert get_by_numar_apartament(lista, 2) == cheltuiala2

    lista = [cheltuiala1, cheltuiala2]

    lista = modificare_cheltuiala(3, 743, '2020-11-15', '', lista)

    assert get_by_numar_apartament(lista, 1) == cheltuiala1
    assert get_by_numar_apartament(lista, 2) == cheltuiala2
