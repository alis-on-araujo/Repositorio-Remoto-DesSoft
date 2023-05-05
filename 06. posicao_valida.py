import revfuncoes

def posicao_valida(frota, linha, coluna, orient, tamanho):

    posicoes = revfuncoes.define_posicoes(linha, coluna, orient, tamanho)

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

'''
O QUE ESSA FUNÇÃO RECEBE
frota = {
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
linha = 6
coluna = 2
orientacao = 'horizontal'
tamanho = 4
resultado = posicao_valida(frota, linha, coluna, orientacao, tamanho)
print(resultado)
'''