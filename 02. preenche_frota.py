import revfuncoes

frota = {}

def preenche_frota(frota, embarcacao, linha, coluna, orient, tamanho):

    if embarcacao not in frota:
        frota[embarcacao] = []

    posicoes = revfuncoes.define_posicoes(linha, coluna, orient, tamanho)

    frota[embarcacao].append(posicoes)

    return frota

'''
O QUE ESSA FUNÇÃO RECEBE
frota = {}
embarcacao = 'navio-tanque'
linha = 6
coluna = 1
orient = 'horizontal'
tamanho = 3

resultado = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
print(resultado)
'''