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

'''
O QUE ESSA FUNÇÃO RECEBE


frota = {
    "porta-aviões":[
      [[1,5],[1,6],[1,7],[1,8]]
    ],
    "navio-tanque":[
      [[6,1],[6,2],[6,3]],
      [[4,7],[5,7],[6,7]]
    ],
    "contratorpedeiro":[
      [[1,1],[2,1]],
      [[2,3],[3,3]],
      [[9,1],[9,2]]
    ],
    "submarino": [
      [[0,3]],
      [[4,5]],
      [[8,9]],
      [[8,4]]
    ],
}
tabuleiro = [
  [0, '-', '-', 1, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 'X', 'X', 'X', 'X', 0],
  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, '-', '-', '-', '-', 0, 0],
  [0, '-', 0, 0, 0, 1, 0, 1, 0, 0],
  [0, 0, 0, 0, '-', 0, 0, 1, 0, 0],
  [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 'X', 0, 0, 0, 0, 1],
  [0, 1, 1, '-', '-', '-', '-', '-', '-', '-']
]
resultado = afundados(frota, tabuleiro)
print(resultado)
'''