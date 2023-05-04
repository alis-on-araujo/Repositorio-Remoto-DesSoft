def afundados(frota, tabuleiro):
    
    afundados= 0
    
    for posicoes in frota.values():

        for coordenadas in posicoes:

            for i , j in coordenadas:

                if tabuleiro[i][j] !='X':
                    break 

            else:
                afundados+=1
    
    return afundados