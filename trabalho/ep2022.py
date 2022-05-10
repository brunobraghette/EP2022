import random
import math
def sorteia_pais(dicio):
    paissorteado, dados = random.choice(list(dicio.items()))
    return  paissorteado
def normaliza(dicio):
    diciofinal = {}
    for dados in dicio.values():
        for pais, info in dados.items():
            diciofinal[pais] = info 
    return diciofinal
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
def sorteia_letra (palavra, lista_restrita):
    restritas = ['.', ',', '-', ';', ' ', "'"]
    palavra = palavra.lower()

    for i in lista_restrita:
        restritas.append(i)

    for j in palavra:
        if j in restritas:
            palavra = palavra.replace(j, '')
                
    if palavra == '':
        return ''
        
    letra = random.choice(palavra)

    while letra in restritas:
        letra = random.choice(palavra)
        
    return letra
tentativas=20
EARTH_RADIUS = 6371
with open('base de dados.py','r')as arquivo:
    conteudo=arquivo.read

#dicas:
d1=
while tentativas>0:
    start=input('1.Tentar acertar(1).\n''2.Loja de dicas(2)')
    if start=='1':
        print('asdjfsasdfas')
    if start=='2':
        loja=input('Você pode comprar as dicas (1) e (2) multiplas vezes.\n{}\n{}\n{}\n{}\n{}'.format(d1,d2,d3,d4,d5))

