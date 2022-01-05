from Domain.cheltuiala import get_numar_apartament,get_data,get_suma,creeaza_cheltuiala,get_tip


def stergere(numar, lista):
    lista_noua=[]
    for c in lista:
        if numar!=get_numar_apartament(c):
            lista_noua.append(c)
    return lista_noua

def adauga_suma(valoare, data, lista):
    lista_noua=[]
    for c in lista:
        suma=get_suma(c)+valoare
        if data==get_data(c):
            cheltuiala=creeaza_cheltuiala(get_numar_apartament(c),suma,get_data(c),get_tip(c))
            lista_noua.append(cheltuiala)
        else:
            lista_noua.append(c)
    return lista_noua

def cea_mai_mare_dupa_tip(tip,lista):
    max=0
    i=0
    for c in lista:
        if get_tip(c)==tip and get_suma(c)>max:
            rez=i
        i=i+1
    return lista[rez]

def descrescator_dupa_suma(lista):
    lista.sort(key=get_suma, reverse=True)
    return lista

def sume_lunare(data1, data2,lista):
    lista_noua= []
    for c in lista:
        if (get_data(c)>=data1 and get_data(c)<=data2):
            lista_noua.append(c)
    return lista_noua