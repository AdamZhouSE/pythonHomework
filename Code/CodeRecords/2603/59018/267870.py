import math
from itertools import combinations

def minkdistance(a,k):
    sums=[]
    b=list(combinations(a,2))
    for j in range(len(b)):
        sums.append(math.abs(b[j][0]-b[j][1]))
    distance=sorted(list(set(sums)))
    print(distance[k-1])
    
    
    
    
    
    
    
a=eval(input())
k=int(input())
minkdistance(a,k)