def define_posicoes(linha, coluna, orient, tam): #recebe linha, coluna, orientação e o tamanho

    ocupados = [] #cria lista das posições ocuoadas

    if orient == 'vertical':

        for i in range(tam):
            ocupados.append([linha + i, coluna])

    if orient == 'horizontal':

        for i in range(tam):
            ocupados.append([linha, coluna + i])

    return ocupados