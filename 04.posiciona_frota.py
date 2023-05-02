def posiciona_frota(frota):
    tabuleiro = [
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
#Percorrendo a lista da frota:
    lista=[]
    for posicoes in frota.values():
        for m  in posicoes:
            for n in m:
                    lista.append(n)


    for i in range( len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            valor= [i,j]
            if valor in lista:
                tabuleiro[i][j]=1       
    return tabuleiro