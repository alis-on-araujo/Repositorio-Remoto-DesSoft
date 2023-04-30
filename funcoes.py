#-----------------------------------------------------------------------------#

#FUNÇÃO 01 - DEFINE POSIÇÕES

def define_posicoes(linha, coluna, orient, tam): #recebe linha, coluna, orientação e o tamanho

    ocupados = [] #cria lista das posições ocupadas

    if orient == 'vertical':

        for i in range(tam):
            ocupados.append([linha + i, coluna])

    if orient == 'horizontal':

        for i in range(tam):
            ocupados.append([linha, coluna + i])

    return ocupados

#-----------------------------------------------------------------------------#

#FUNÇÃO 02 - PREENCHE FROTA

def preenche_frota(frota, nome, linha, coluna, orientacao, tamanho):

    if nome not in frota:
        frota[nome] = []

    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    
    frota[nome].append(posicoes)

    return frota