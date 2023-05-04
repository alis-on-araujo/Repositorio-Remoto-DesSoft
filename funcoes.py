#-----------------------------------------------------------------------------#

#FUNÇÃO 01 - DEFINE POSIÇÕES

tabuleiro = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]


def define_posicoes(linha, coluna, orient, tam): #recebe linha, coluna, orientação e o tamanho

    ocupados = [] #cria lista das posições ocuoadas

    if orient == 'vertical':

        for i in range(tam):
            ocupados.append([linha + i, coluna])
            tabuleiro[linha + i][coluna] += 1

    if orient == 'horizontal':

        for i in range(tam):
            ocupados.append([linha, coluna + i])
            tabuleiro[linha][coluna + i] += 1

    return ocupados

#-----------------------------------------------------------------------------#

#FUNÇÃO 02 - PREENCHE FROTA

def preenche_frota(frota, nome, linha, coluna, orientacao, tamanho):

    if nome not in frota:
        frota[nome] = []

    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    
    frota[nome].append(posicoes)

    return frota

#-----------------------------------------------------------------------------#

#FUNÇÃO 03 - FAZ JOGADA

def faz_jogada(tabuleiro, linha, coluna):

    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'

    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro

#-----------------------------------------------------------------------------#

#FUNÇÃO 04 - POSICIONA FROTA

def posiciona_frota(frota):

    tabuleiro_posiciona = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
    ]

    for posicoes in frota.values():
        for posicao in posicoes:
            for linha, coluna in posicao:
                tabuleiro_posiciona[linha][coluna] = 1

    return tabuleiro_posiciona

#-----------------------------------------------------------------------------#

#FUNÇÃO 05 - QUANTAS EMBARCAÇÕES AFUNDADAS

def afundados(frota, tabuleiro):
    
    afundados= 0
    
    for posicoes in frota.values():

        for coordenadas in posicoes:

            for i , j in coordenadas:

                if tabuleiro[i][j] !='X':
                    break 

            else:
                afundados+=1
    
    return afundados