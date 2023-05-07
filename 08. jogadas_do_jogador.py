import revfuncoes

from revfuncoes import frota

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

tabuleiro_oponente = revfuncoes.posiciona_frota(frota_oponente)

tabuleiro_jogador = revfuncoes.posiciona_frota(frota)

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
    inedito = False
    continua = True

    while continua == True:
        
        inedito = False

        while inedito == False:

            valido_linha = False

            while valido_linha == False:

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
                    valido_linha = False

                else:
                    valido_linha = True

            if valido_linha == True and valido_coluna == True:

                if jogadas[linha_ataque, coluna_ataque] not in jogadas:
                    jogadas.append([linha_ataque, coluna_ataque])

                    inedito = True

                    valido_coluna = False
                    valido_linha = False
                
                else:
                    print(f'A posição linha {linha_ataque} e coluna {coluna_ataque} já foi informada anteriormente!')

                    inedito = False

        tabuleiro_oponente = revfuncoes.faz_jogada(tabuleiro_oponente, linha_ataque, coluna_ataque)

        if revfuncoes.afundados(tabuleiro_oponente, frota_oponente):
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
            continua = False
            jogando = False