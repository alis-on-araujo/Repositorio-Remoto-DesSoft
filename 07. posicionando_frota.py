import revfuncoes as rf
from revfuncoes import frota

embarcacoes = {
    "porta-aviões": 1,
    "navio-tanque": 2,
    "contratorpedeiro": 3,
    "submarino": 4,
}

tamanhos = {
    "porta-aviões": 4,
    "navio-tanque": 3,
    "contratorpedeiro": 2,
    "submarino": 1,
}

for embarcacao, quantidade in embarcacoes.items():
    tamanho = tamanhos[embarcacao]

    for i in range(quantidade):

        posicao = False

        while not posicao:

            
            print("Insira as informações referentes ao navio {0} que possui tamanho {1}".format(embarcacao, tamanho))
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if embarcacao == "submarino":
                orient = "vertical"

            elif embarcacao != "submarino":
                orient = input("[1] Vertical [2] Horizontal >")
                if orient == '1':
                    orient = 'vertical'
                elif orient == '2':
                    orient = 'horizontal'

            if rf.posicao_valida(frota, linha, coluna, orient, tamanho):
                rf.preenche_frota(frota, embarcacao, linha, coluna, orient, tamanho)
                posicao = True

            elif not rf.posicao_valida(frota, linha, coluna, orient, tamanho):
                print("Esta posição não está válida!")
                posicao = False
                        
print(frota)