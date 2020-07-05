from itertools import combinations

def minkdistance(a,k):
    sums=[]
    b=list(sombinations(a,2))
    for j in range(len(b)):
        sums.append(sum(b[j]))
    distance=sorted(list(set(sums)))
    print(distance[k-1])
    
    
    
    
    
    
    
a=eval(input())
k=int(input())