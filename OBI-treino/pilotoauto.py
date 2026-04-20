# A = int(input())
# B = int(input())
# C = int(input())
# if (B-A) == (B-C):
#     print(0)
# elif (B-A) < (B-C):
#     print(1)
# elif (B-A) > (B-C):
#     print(-1)


lista = []
for i in range(3):
    N = int(input())
    lista.append(N)
dist_BA = lista[1] - lista[0]
dist_CB = lista[2] - lista[1]

if dist_BA < dist_CB:
    print(1)
elif dist_BA > dist_CB:
    print(-1)
else:
    print(0)