import funcoes

def posicao_valida(frota, linha, coluna, orient, tam):

    posicoes = funcoes.define_posicoes(linha, coluna, orient, tam)
    maximo = 9
    minimo = 0

    for posicao in posicoes:
        x, y = posicao

        if x < minimo or y < minimo or x > maximo or y > maximo:
            return False
    
    for coords in frota.values():
        for coord in coords:
            for x, y in coord:
                if [x, y] in posicoes:
                    return False

    return True
