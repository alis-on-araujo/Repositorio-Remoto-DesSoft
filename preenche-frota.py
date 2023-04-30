import funcoes

def preenche_frota(frota, nome, linha, coluna, orientacao, tamanho):

    if nome not in frota:
        frota[nome] = []

    posicoes = funcoes.define_posicoes(linha, coluna, orientacao, tamanho)
    
    frota[nome].append(posicoes)

    return frota