import random
import math
#vai precisar da normaliza p dicas
def normaliza(dicio):
    diciofinal = {}
    for dados in dicio.values():
        for pais, info in dados.items():
            diciofinal[pais] = info 
    return diciofinal
#sorteador com normaliza dentro 
def sorteia_pais(dicio):
    diciofinal = {}
    for dados in dicio.values():
        for pais, info in dados.items():
            diciofinal[pais] = info 
    paissorteado, dados = random.choice(list(diciofinal.items()))
    return  paissorteado

import math
#latA = latitude do ponto A
#longA = longitutde do ponto A
#latb = latitiude do ponto B 
#longb = longitude do ponto B
def haversine (r, latA, longA, latB, longB):
    latAr = math.radians(latA)
    longAr = math.radians(longA)
    latBr = math.radians(latB)
    longBr = math.radians(longB)
    x = 2*r
    
    raiz  = (math.sin((latBr -latAr)/2))*2 + math.cos(latAr) * math.cos(latBr) *( math.sin((longBr-longAr)/2))*2
    parenteses = math.asin(math.sqrt(raiz))
    d = x * parenteses
    return d
def esta_na_lista(pais, lista):
    for i in range(len(lista)):
        if pais in lista[i]:
            return True
    else:
        return False
def sorteia_letra (palavra):
    lista_restritas = []
    palavra = palavra.lower()
    lista_de_lestras=list(palavra)
    letra_sorteada=random.choice(lista_de_lestras)
    if letra_sorteada not in lista_restritas:
            lista_restritas.append(letra_sorteada)
            lista_de_lestras.remove(letra_sorteada)
    return lista_restritas

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
tentativas=20
EARTH_RADIUS = 6371
with open('base de dados.py','r')as arquivo:
    conteudo=arquivo.read


#dicas:
d1='1. Cor da Bandeira - Preço: 4 tentativas'
d2='2. Letra da Capital - Preço: 3 tentativas'
d3='3. Área - Preço: 6 tenativas'
d4="4. População - Preço: 5 tenativas "
d5="5.Continente - Preço: 7 tentativas/n"
d0='Voltar'
while tentativas>0:
    start=input('1.Tentar acertar(1).\n''2.Loja de dicas(2)')
    if start=='1':
        print('asdjfsasdfas')
    if start=='2':
        loja=input('Você pode comprar as dicas (1) e (2) multiplas vezes.\n{}\n{}\n{}\n{}\n{}\n{}'.format(d1,d2,d3,d4,d5,d0))
