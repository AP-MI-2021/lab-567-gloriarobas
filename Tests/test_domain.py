from Domain.cheltuiala import get_numar_apartament, get_tip,get_data,get_suma, creeaza_cheltuiala

def test_domeniu():
    cheltuiala = creeaza_cheltuiala(1, 123, '2020-12-12', 'intretinere')

    assert get_numar_apartament(cheltuiala) == 1
    assert get_suma(cheltuiala) == 123
    assert get_data(cheltuiala) == '2020-12-12'
    assert get_tip(cheltuiala) == 'intretinere'
