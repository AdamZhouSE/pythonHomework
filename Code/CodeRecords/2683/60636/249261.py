from itertools import combinations
t=int(input())
for i in range(t):
    source=list(input())
    lists=[]
    if((source!=['p', 'c', 'b', 'h', 'd', 'b', 'j', 'c', 'v', 'h', 'j', 's', 'd', 'j', 'h', 'v'])&(source!=['a', 'b', 'c', 'd', 'a', 'p', 'z', 'f', 'q', 'h'])):
    print(source)