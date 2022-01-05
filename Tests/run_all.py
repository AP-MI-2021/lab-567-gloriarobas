from Tests.test_crud import test_adauga_cheltuiala, test_sterge_cheltuiala, test_modifica_cheltuiala
from Tests.test_domain import test_domeniu
from Tests.test_functionalitati import test_stergere,test_adauga_suma,test_cea_mai_mare_dupa_tip,test_descrescator_dupa_suma, test_sume_lunare


def run_all_tests():
    test_domeniu()
    test_adauga_cheltuiala()
    test_sterge_cheltuiala()
    test_modifica_cheltuiala()
    test_stergere()
    test_adauga_suma()
    test_cea_mai_mare_dupa_tip()
    test_descrescator_dupa_suma()
    test_sume_lunare()
