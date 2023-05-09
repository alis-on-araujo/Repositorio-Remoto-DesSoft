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

        print("Insira as informações referentes ao navio {0} que possui tamanho {1}".format(embarcacao, tamanho))

        posicao = False

        while not posicao:

            linha = input("Linha: ")
            coluna = input("Coluna: ")

            if embarcacao == "submarino":
                orient = "vertical"

            elif embarcacao != "submarino":
                orient = input("[1] Vertical [2] Horizontal >")

            if posicao_valida(frota, linha, coluna, orient, tamanho):
                preenche_frota(frota, embarcacao, linha, coluna, orient, tamanho)
                posicao = True

            elif not posicao_valida(frota, linha, coluna, orient, tamanho):
                while not posicao_valida(frota, linha, coluna, orient, tamanho):
                    print("Posição inválida, tente novamente.")
                    linha = input("Linha: ")
                    coluna = input("Coluna: ")

                    if embarcacao == "submarino":
                        orient = "vertical"

                    elif embarcacao != "submarino":
                        orient = input("[1] Vertical [2] Horizontal >")
                        
print(frota)
posiciona_frota(frota)

