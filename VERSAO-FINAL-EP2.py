#PASSOU NOS TESTES!!!!!!!!!!!!!!!!!!!!!!!!!
#Para versão mais bonita checar revfuncoes.py


import random

#random.seed(2)

def define_posicoes(linha, coluna, orient, tamanho): 

    linha = int(linha)
    coluna = int(coluna)

    ocupados = [] 

    if orient == 'vertical':

        for i in range(tamanho):
            ocupados.append([int(linha + i), int(coluna)])

    if orient == 'horizontal':

        for i in range(tamanho):
            ocupados.append([int(linha), int(coluna + i)])

    return ocupados

frota = {}

def preenche_frota(frota, embarcacao, linha, coluna, orient, tamanho):

    if embarcacao not in frota:
        frota[embarcacao] = []

    posicoes = define_posicoes(linha, coluna, orient, tamanho)

    frota[embarcacao].append(posicoes)

    return frota

def faz_jogada(tabuleiro, linha, coluna):

    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'

    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro


def posiciona_frota(frota):

    tabuleiro_posiciona = [
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

    for lista_posicoes in frota.values():

        for posicao in lista_posicoes:

            for linha, coluna in posicao:

                tabuleiro_posiciona[linha][coluna] = 1

    return tabuleiro_posiciona


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


def posicao_valida(frota, linha, coluna, orient, tamanho):

    posicoes = define_posicoes(linha, coluna, orient, tamanho)

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

            if posicao_valida(frota, linha, coluna, orient, tamanho):
                preenche_frota(frota, embarcacao, linha, coluna, orient, tamanho)
                posicao = True

            elif not posicao_valida(frota, linha, coluna, orient, tamanho):
                print("Esta posição não está válida!")
                posicao = False

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)

tabuleiro_jogador = posiciona_frota(frota)

jogando = True

while jogando:

    def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '_______________________________      _______________________________\n'

        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
        return texto


    jogadas = []
    jogadas_oponente = []
    inedito = False
    continua = True

    while continua == True:
        
        inedito = False

        while inedito == False:

            valido_linha = False

            while valido_linha == False:
                print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
                linha_ataque = int(input('Jogador, qual linha deseja atacar? '))

                if linha_ataque > 9 or linha_ataque < 0:
                    print('Linha inválida!')
                    valido_linha = False

                else:
                    valido_linha = True

            valido_coluna = False

            while valido_coluna == False:
                
                coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))

                if coluna_ataque > 9 or coluna_ataque < 0:
                    print('Coluna inválida!')
                    valido_coluna = False

                else:
                    valido_coluna = True

            if valido_linha == True and valido_coluna == True:
                

                if [linha_ataque, coluna_ataque] not in jogadas:
                    jogadas.append([linha_ataque, coluna_ataque])

                    inedito = True

                    valido_coluna = False
                    valido_linha = False
                
                else:
                    print(f'A posição linha {linha_ataque} e coluna {coluna_ataque} já foi informada anteriormente!')
                    
                    inedito = False

        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_ataque, coluna_ataque)
        
        if afundados(frota_oponente, tabuleiro_oponente) == 10:
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
            continua = False
            jogando = False
        
        else:

            valido_oponente = False

            while valido_oponente == False:
                
                linha_oponente = random.randint(0, 9)
                coluna_oponente = random.randint(0, 9)

                if [linha_oponente, coluna_oponente] not in jogadas_oponente:
                        jogadas_oponente.append([linha_oponente, coluna_oponente])
                        print(f'Seu oponente está atacando na linha {linha_oponente} e coluna {coluna_oponente}')
                        valido_oponente = True

            tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_oponente, coluna_oponente)

            if afundados(frota, tabuleiro_jogador) == 10:
                print('Xi! O oponente derrubou toda a sua frota =(')
                continua = False
                jogando = False