linha_ataque= 1
coluna_ataque=2
jogadas=[[1,2]]
if [linha_ataque, coluna_ataque] not in jogadas:
                    jogadas.append([linha_ataque, coluna_ataque])

print(jogadas)