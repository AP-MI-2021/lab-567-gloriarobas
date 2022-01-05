from Logic.functionalitati import stergere,adauga_suma,cea_mai_mare_dupa_tip,descrescator_dupa_suma, sume_lunare
from Domain.cheltuiala import creeaza_cheltuiala,get_suma

def test_stergere():
    cheltuiala1 = creeaza_cheltuiala(1, 147, '2020-10-11', 'alte cheltuieli')
    cheltuiala2 = creeaza_cheltuiala(1, 123, '2020-12-12', 'intretinere')
    cheltuiala3 = creeaza_cheltuiala(2, 130, '2020-09-07', 'intretinere')
    lista = [cheltuiala1, cheltuiala2, cheltuiala3]
    assert len(stergere(1,lista)) == 1

def test_adauga_suma():
    cheltuiala1 = creeaza_cheltuiala(1, 147, '2020-10-11', 'alte cheltuieli')
    cheltuiala2 = creeaza_cheltuiala(1, 123, '2020-12-12', 'intretinere')
    cheltuiala3 = creeaza_cheltuiala(2, 130, '2020-10-11', 'intretinere')
    lista = [cheltuiala1, cheltuiala2, cheltuiala3]
    assert len(adauga_suma(10,'2020-10-11',lista)) == 3
    rezultat=adauga_suma(10,'2020-10-11',lista)
    assert get_suma(rezultat[0])==157
    assert get_suma(rezultat[1]) == 123
    assert get_suma(rezultat[2]) == 140

def test_cea_mai_mare_dupa_tip():
    cheltuiala1 = creeaza_cheltuiala(1, 147, '2020-10-11', 'alte cheltuieli')
    cheltuiala2 = creeaza_cheltuiala(1, 123, '2020-12-12', 'intretinere')
    cheltuiala3 = creeaza_cheltuiala(2, 130, '2020-10-11', 'intretinere')
    lista = [cheltuiala1, cheltuiala2, cheltuiala3]
    rezultat = cea_mai_mare_dupa_tip('intretinere',lista)
    assert get_suma(rezultat)==130

def test_descrescator_dupa_suma():
    cheltuiala1 = creeaza_cheltuiala(1, 147, '2020-10-11', 'alte cheltuieli')
    cheltuiala2 = creeaza_cheltuiala(1, 123, '2020-12-12', 'intretinere')
    cheltuiala3 = creeaza_cheltuiala(2, 130, '2020-10-11', 'intretinere')
    lista = [cheltuiala1, cheltuiala2, cheltuiala3]
    rezultat=descrescator_dupa_suma(lista)
    assert get_suma(rezultat[0]) == 147
    assert get_suma(rezultat[1]) == 130
    assert get_suma(rezultat[2]) == 123

def test_sume_lunare():
    cheltuiala1 = creeaza_cheltuiala(1, 147, '2020-10-11', 'alte cheltuieli')
    cheltuiala2 = creeaza_cheltuiala(1, 123, '2020-12-12', 'intretinere')
    cheltuiala3 = creeaza_cheltuiala(2, 130, '2020-10-11', 'intretinere')
    lista = [cheltuiala1, cheltuiala2, cheltuiala3]
    rezultat = sume_lunare('2020-10-1','2020-10-30',lista)
    assert get_suma(rezultat[0]) == 147
    assert get_suma(rezultat[1]) == 130