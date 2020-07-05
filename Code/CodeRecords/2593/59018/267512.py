from itertools import combinations
from collections import defaultdict
def addtuple(N,a):
    dict=defaultdict(list)
    a=list(combinations(a,2))
    for j in range(N):
        dict[sum(a[j])].append(a[j])
    list1=sorted(dict.items())
    print(list1[0])
        
        
        
    
    
    
    
    
    
    
    
    
    
T=int(input())
for i in range(T):
    N=int(input())
    info1=input().split(', ')
    a=[int(y) for y in info1]
    addtuple(N,a)