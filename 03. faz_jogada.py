def faz_jogada(tabuleiro, linha, coluna):

    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'

    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro

'''
O QUE ESSA FUNÇÃO RECEBE
tabuleiro = [
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
  [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
]

linha = 1
coluna = 1
resultado = faz_jogada(tabuleiro, linha, coluna)
print(resultado)
'''