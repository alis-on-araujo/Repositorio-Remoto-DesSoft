### INFORMAÇÕES
# linha = onde será posicionada a embarcação
# coluna = coluna onde será posicionada a embarcação
# orient = orientação (str)
# tamanho = tamanho da embarcação
# embarcacao = nome do navio
# posicao = [linha][coluna]
# afundados = quantidade de barcos afundados

### RETORNANDO OUTRAS FUNCOES
# posicoes = define_posicoes(linha, coluna, orient, tamanho)

### LISTAS
# ocupados = lista com as posições que os navios estão ocupando
# lista_posicoes = valores do dicionario frota[embarcacao]

### DICIONÁRIOS
# frota = dicionário com cada navio e as posições que está ocupando

### FUNÇÕES

# define_posicoes(linha, coluna, orient, tamanho)
    #retorna a posição

# preenche_frota(frota, embarcacao, linha, coluna, orient, tamanho)
    #retorna o dicionário frota

# faz_jogada(tabuleiro, linha, coluna)
    #retorna o tabuleiro com x e -

# posiciona_frota(frota)
    #retorna o tabuleiro com 1 e 0

# afundados(frota, tabuleiro)
    #retorna a quantidade de navios afundados (afundados)

### TABULEIROS
# tabuleiro = tabuleiro respondido com x e -
# tabuleiro_posiciona = tabuleiro com as posições do navio
#-----------------------------------------------------------------------------#

#FUNÇÃO 01 - DEFINE POSIÇÕES

def define_posicoes(linha, coluna, orient, tamanho): 

    ocupados = [] 

    if orient == 'vertical':

        for i in range(tamanho):
            ocupados.append(([int(linha) + i, int(coluna)]))

    if orient == 'horizontal':

        for i in range(tamanho):
            ocupados.append([linha, coluna + i])

    return ocupados


#-----------------------------------------------------------------------------#

#FUNÇÃO 02 - PREENCHE FROTA

frota = {}

def preenche_frota(frota, embarcacao, linha, coluna, orient, tamanho):

    if embarcacao not in frota:
        frota[embarcacao] = []

    posicoes = define_posicoes(linha, coluna, orient, tamanho)

    frota[embarcacao].append(posicoes)

    return frota


#-----------------------------------------------------------------------------#

#FUNÇÃO 03 - FAZ JOGADA

def faz_jogada(tabuleiro, linha, coluna):

    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'

    elif tabuleiro[linha][coluna] == 0:
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

    for lista_posicoes in frota.values():

        for posicao in lista_posicoes:

            for linha, coluna in posicao:

                tabuleiro_posiciona[linha][coluna] = 1

    return tabuleiro_posiciona



#-----------------------------------------------------------------------------#

#FUNÇÃO 05 - QUANTAS EMBARCAÇÕES AFUNDADAS

def afundados(frota, tabuleiro):
    
    afundados = 0
    
    for posicoes in frota.values():

        for coordenadas in posicoes:

            for linha , coluna in coordenadas:

                if tabuleiro[linha][coluna] !='X':
                    break 

            else:
                afundados += 1
    
    return afundados


#-----------------------------------------------------------------------------#

#FUNÇÃO 06 - POSIÇÃO VÁLIDA

def posicao_valida(frota, linha, coluna, orient, tamanho):

    posicoes = define_posicoes(linha, coluna, orient, tamanho)

    maximo = 9
    minimo = 0

    for posicao in posicoes:
        
        linha, coluna = posicao

        if linha < minimo or coluna < minimo or linha > maximo or coluna > maximo:
            return False
    
    for lista_posicoes in frota.values():

        for posicao in lista_posicoes:

            for linha, coluna in posicao:

                if [linha, coluna] in posicoes:
                    return False

    return True


#-----------------------------------------------------------------------------#

#FUNÇÃO 07 - POSICIONANDO FROTA