def creeaza_cheltuiala(numar_apartament, suma, data, tip):
    '''
    creeaza o cheltuiala
    :param numar_apartament: int
    :param suma: int
    :param data: date
    :param tip: intretinere, canal, alte cheltuieli
    :return:
    '''
    return {
        "numar_apartament": numar_apartament,
        "suma": suma,
        "data": data,
        "tip": tip,
    }

def get_numar_apartament(cheltuiala):
    return cheltuiala['numar_apartament']


def get_suma(cheltuiala):
    return cheltuiala['suma']


def get_data(cheltuiala):
    return cheltuiala['data']


def get_tip(cheltuiala):
    return cheltuiala['tip']

def to_string(cheltuiala):
    return "numar_apartament: {}, suma: {}, data: {}, tip: {} ".format(
        get_numar_apartament(cheltuiala),
        get_suma(cheltuiala),
        get_data(cheltuiala),
        get_tip(cheltuiala)
    )