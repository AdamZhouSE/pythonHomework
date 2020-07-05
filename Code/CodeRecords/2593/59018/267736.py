from itertools import combinations
from collections import defaultdict
def addtuple(N,a):
    dict=defaultdict(list)
    a=list(combinations(a,2))
    for j in range(N):
        dict[sum(a[j])].append(a[j])
    list1=sorted(dict.items())
    for j in range(len(list1)):
        if len(list1[j][1])==2:
            print(
        
        
        
    
    
    
    
    
    
    
    
    
    
T=int(input())
for i in range(T):
    N=int(input())
    info1=input().split(', ')
    a=[int(y) for y in info1]
    addtuple(N,a)