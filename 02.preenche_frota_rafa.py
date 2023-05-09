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
    
    posicoes = define_posicoes(linha, coluna, orient, tamanho)
    
    if embarcacao not in frota:
        frota[embarcacao]=[]
        if posicoes not in frota[embarcacao]:
        
            frota[embarcacao] = posicoes
    else:

        frota[embarcacao]+=posicoes

    return frota

frota = {
  "navio-tanque":[
    [[6,1],[6,2],[6,3]]
  ]
}
nome_navio = 'navio-tanque'
linha = 4
coluna = 7
orientacao = 'vertical'
tamanho = 3