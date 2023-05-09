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


def preenche_frota(frota, embarcacao, linha, coluna, orient, tamanho):

    frota = {}
    resultado=[]
    posicoes = define_posicoes(linha, coluna, orient, tamanho)
    resultado.append()
    if embarcacao not in frota:
        resultado.append(posicoes)
        frota[embarcacao] = resultado
    else:

        frota[embarcacao]+=posicoes

    return frota