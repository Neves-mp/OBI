
t1 = int(input()) 
t2 = int(input())  
t3 = int(input())  
nadadores = [
    (t1, 1), 
    (t2, 2), 
    (t3, 3) 
]
nadadores.sort()
print(nadadores[0][1])
print(nadadores[1][1])
print(nadadores[2][1])