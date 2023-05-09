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

frota = {}

def preenche_frota(frota, embarcacao, linha, coluna, orient, tamanho):

    if embarcacao not in frota:
        frota[embarcacao] = []

    posicoes = define_posicoes(linha, coluna, orient, tamanho)

    frota[embarcacao].append(posicoes)

    return frota


frota = {}
embarcacao = 'navio-tanque'
linha = 6
coluna = 1
orient = 'horizontal'
tamanho = 3

resultado = preenche_frota(frota, embarcacao, linha, coluna, orient, tamanho)
print(resultado)
