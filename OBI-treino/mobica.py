M = int(input())
filho1 = int(input())
filho2 = int(input())
filho3 = M - filho1 - filho2
idades = [filho1, filho2, filho3]
idades.sort()
print(idades[2])