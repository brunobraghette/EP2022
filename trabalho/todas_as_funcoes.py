def normaliza(dicio):
    diciofinal = {}
    for dados in dicio.values():
        for pais, info in dados.items():
            diciofinal[pais] = info 
    return diciofinal

import random 
def sorteia_pais(dicio):
    paissorteado, dados = random.choice(list(dicio.items()))
    return  paissorteado


def adiciona_em_ordem(pais, dist, lista):
    x = [pais, dist]
    j=0
    if pais in lista:
        return lista 
    if len(lista) == 0:
        lista.append(x)
    elif pais not in lista:
        for i in range(len(lista)):
            if lista[i][1]<dist:
                j+=1
            if lista [i][1]>dist:
                lista.insert(j, x)
                break
    return lista


import math
def haversine (r, ro1, epsi1, ro2, epsi2):
    ro1r = math.radians(ro1)
    epsi1r = math.radians(epsi1)
    ro2r = math.radians(ro2)
    epsi2r = math.radians(epsi2)
    x = 2*r
    
    raiz  = (math.sin((ro2r -ro1r)/2))*2 + math.cos(ro1r) * math.cos(ro2r) *( math.sin((epsi2r-epsi1r)/2))*2
    parenteses = math.asin(math.sqrt(raiz))
    d = x * parenteses
    return d

def esta_na_lista(pais, lista):
    for i in range(len(lista)):
        if pais in lista[i]:
            return True
    else:
        return False

def adiciona_em_ordem(pais, dist, lista):
    x = [pais, dist]
    j=0
    if pais in lista:
        return lista 
    if len(lista) == 0:
        lista.append(x)
    elif pais not in lista:
        for i in range(len(lista)):
            if lista[i][1]<dist:
                j+=1
            if lista [i][1]>dist:
                lista.insert(j, x)
                break
    return lista