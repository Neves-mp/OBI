l1 = int(input())
l2 = int(input())
c1 = int(input())
c2 = int(input())
Lia = 0
Carolina = 0

if l1 == l2:
    Lia = (l1 + l2)*2 

elif l2 == l1+1 or l2 == l1-1:
    Lia = (l1 + l2)*3

#se quiser simplificar, pode ser simplesmente else
else:
    Lia = l1 + l2
# a condicional acima sendo positiva, não continua rodando o elif abaixo.

#inicia um novo if elif 
if c1 == c2:
    Carolina = (c1 + c2)*2 

elif c1 == c2+1 or c1 == c2-1:
    Carolina = (c1 + c2)*3

elif c1 != c2:
    Carolina = c1 + c2
#inicia um novo if
if Lia > Carolina:
    print("Lia")
elif Lia < Carolina:
    print("Carolina")
elif Lia == Carolina:
    print("empate")
