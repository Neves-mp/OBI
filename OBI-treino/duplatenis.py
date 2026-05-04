jogadores = []
for i in range(4):
    jogador = int(input())
    jogadores.append(jogador)
jogadores.sort
dupla1 = jogadores[0] + jogadores[3]
dupla2 = jogadores[1] + jogadores[2]
saida = dupla1 - dupla2
print(abs(saida))
