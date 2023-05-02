def afundados(frota, tabuleiro):
    
    afundados= 0
    for valores  in frota.values():
        for cordenadas in valores:
            for i , j in cordenadas:
                if  tabuleiro[i][j]!='X':
                    break 

            else:
                afundados+=1
    
    
    
    return afundados