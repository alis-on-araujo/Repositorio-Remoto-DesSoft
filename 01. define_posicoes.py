#FUNÇÃO 01 - DEFINE POSIÇÕES

def define_posicoes(linha, coluna, orient, tamanho): 

    ocupados = [] 

    if orient == 'vertical':

        for i in range(tamanho):
            ocupados.append([linha + i, coluna])

    if orient == 'horizontal':

        for i in range(tamanho):
            ocupados.append([linha, coluna + i])

    return ocupados

'''
O QUE ESSA FUNÇÃO RECEBE
linha = 2
coluna = 4
orientacao = "vertical"
tamanho = 3

print(define_posicoes(linha, coluna, orientacao, tamanho))
'''
