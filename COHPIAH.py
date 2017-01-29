import re
import math


########  FUNÇÕES DADAS NO EX  ######################################

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    frase = re.split(r'[,:;]+', sentenca)
    return frase

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    palavra = frase.split()
    return palavra

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que
    aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras
    diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    diferentes = len(freq)
    return diferentes


########  FUNÇÕES AUXILIARES  #######################################

def menor(lista):
    min = 999999
    i = 0
    while i < len(lista):
        if lista[i] < min:
            min = lista[i]
        i = i + 1
    return min


def lista_sentencas(texto):
    listaSentencas = separa_sentencas(texto)
    return listaSentencas


def lista_frases(texto):
    listaFrases = []
    listaSentencas = separa_sentencas(texto)    
    i = 0
    while i < len(listaSentencas):
        listaFrases = separa_frases(listaSentencas[i]) + listaFrases
        i = i + 1
    return listaFrases


def lista_palavras(texto):
    listaPalavras = []
    j = 0
    listaFrases = lista_frases(texto)
    while j < len(listaFrases):
        listaPalavras = separa_palavras(listaFrases[j]) + listaPalavras
        j = j + 1
    return listaPalavras



########  FUNÇÕES DOS ÍNDICES  ######################################


# Tamanho médio de palavra é a soma dos tamanhos das
# palavras dividida pelo número total de palavras.
def calcWAL(texto):
    listaDePalavras = lista_palavras(texto)
    i = 0
    somaLetra = 0
    while i < len(listaDePalavras):
        somaLetra = len(listaDePalavras[i]) + somaLetra
        i = i + 1
    WAL = somaLetra/len(listaDePalavras)
    return WAL


# Relação Type-Token: Número de palavras diferentes
# utilizadas em um texto divididas pelo total de palavras.
def calcTTR(texto):
    listaDePalavras = lista_palavras(texto)
    TTR = n_palavras_diferentes(listaDePalavras) / len(listaDePalavras)
    return TTR


# Razão Hapax Legomana: Número de palavras utilizadas uma
# vez dividido pelo número total de palavras.
def calcHLR(texto):
    listaDePalavras = lista_palavras(texto)
    HLR = n_palavras_unicas(listaDePalavras) / len(listaDePalavras)
    return HLR


# Tamanho médio de sentença é a soma dos números de caracteres
# em todas as sentenças dividida pelo número de sentenças.
def calcSAL(texto):
    listaSentencas = lista_sentencas(texto)
    somaLetra = 0
    for item in listaSentencas:
        somaLetra = len(item) + somaLetra
    SAL = somaLetra / len(listaSentencas)
    return SAL


#Complexidade de sentença: Média simples
# do número de frases por sentença.
def calcSAC(texto):
    listaFrases = lista_frases(texto)
    listaSentencas = lista_sentencas(texto)
    SAC = len(listaFrases) / len(listaSentencas)
    return SAC


# Tamanho médio da frase é a soma do número de caracteres 
# em cada frase dividida pelo número de frases no texto.
def calcPAL(texto):
    listaFrases = lista_frases(texto)
    listaPalavras = lista_palavras(texto)
    somaLetras = 0
    for item in listaFrases:
        somaLetras = len(item) + somaLetras    
    PAL =  somaLetras / len(listaFrases)
    return PAL



########  FUNÇÕES PARA IMPLEMENTAR  #################################

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o 
    grau de similaridade nas assinaturas.'''
    i = 0
    difer = 0
    while i < 6:
        difer = math.sqrt(( as_a[i] - as_b[i] ) **2 ) + difer
        i = i + 1
    media = difer / 6
    return media


def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    return [calcWAL(texto), calcTTR(texto), calcHLR(texto), \
    calcSAL(texto), calcSAC(texto), calcPAL(texto)]


def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e deve devolver o numero 
    (0 a n-1) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    listaAss =[]
    listaCompa = []
    for tex in textos:
        listaAss.append(calcula_assinatura(tex))
    for vetor in listaAss:
        listaCompa.append(compara_assinatura(ass_cp, vetor))
    textoMenorAss = listaCompa.index(menor(listaCompa))
    return textoMenorAss



########  FUNÇÕES DE TESTE  #########################################

def programa():
    #   assOrig = le_assinatura()
    assOrig = [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]
    vetorTextos = le_textos()
    
    numeroDoTexto = avalia_textos(vetorTextos, assOrig) + 1
    print("vetorOriginal", assOrig, "\n")

    print("vetorTex1", calcula_assinatura(vetorTextos[0]))
    print("vetorTex2", calcula_assinatura(vetorTextos[1]))
    print("vetorTex3", calcula_assinatura(vetorTextos[2]), "\n")

    print("avalia", avalia_textos(vetorTextos, assOrig))
    print("numeroDoTexto:", numeroDoTexto)
    print("O autor do texto {} esta infectado com COH-PIAH".format(numeroDoTexto))

def calcTUDO(texto):
    print("Num de caracteres =", len(texto))
    print("Total Palavras =", len(lista_palavras(texto)))
    print("Frases =", len(lista_frases(texto)))    
    print("Sentenças =", len(lista_sentencas(texto)))
    print("Palavras Diferentes =", n_palavras_diferentes(lista_palavras(texto)))
    print("Palavras Únicas =", n_palavras_unicas(lista_palavras(texto)), "\n")

    print("WAL =", calcWAL(texto))
    print( "(Num de caracteres / Total Palavra)\n")

    print("TTR =", calcTTR(texto))
    print( "(Palavras Diferentes / Total Palavras)\n")

    print("HLR =", calcHLR(texto))
    print( "(Palavras Únicas / Total Palavras)\n")

    print("SAL =", calcSAL(texto))
    print( "(Num de caracteres / Sentenças)\n")

    print("SAC =", calcSAC(texto))
    print( "(Frases / Sentenças)\n")

    print("PAL =", calcPAL(texto))
    print( "(Num de caracteres / Frases)\n")

def calcTUDOvetor(texto):
    return [calcWAL(texto), calcTTR(texto), calcHLR(texto), \
     calcSAL(texto), calcSAC(texto), calcPAL(texto)]



###########  O PROGRAMA PRA VALER! ##################################

assOrig = le_assinatura()
vetorTextos = le_textos()

numeroDoTexto = avalia_textos(vetorTextos, assOrig) + 1

print("O autor do texto {} esta infectado com COH-PIAH".format(numeroDoTexto))