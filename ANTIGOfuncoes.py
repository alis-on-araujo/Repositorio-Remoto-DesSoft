#-----------------------------------------------------------------------------#

#FUNÇÃO 01 - DEFINE POSIÇÕES

def define_posicoes(linha, coluna, orient, tam): 

    ocupados = [] 

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
                afundados += 1
    
    return afundados

#-----------------------------------------------------------------------------#

#FUNÇÃO 06 - POSIÇÃO VÁLIDA

def posicao_valida(frota, linha, coluna, orient, tam):

    posicoes = define_posicoes(linha, coluna, orient, tam)
    maximo = 9
    minimo = 0

    for posicao in posicoes:
        
        x, y = posicao

        if x < minimo or y < minimo or x > maximo or y > maximo:
            return False
    
    for coords in frota.values():

        for coord in coords:

            for x, y in coord:

                if [x, y] in posicoes:
                    return False

    return True