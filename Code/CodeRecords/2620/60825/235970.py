import math

n=int(input())
for i in range(n):
    N=int(input())
    res=0
    
    i=1
    while i<=N:
        res+=math.pow(i,5)
        i+=1
        
    print(int(res))