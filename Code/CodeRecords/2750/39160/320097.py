import collections

n = int(input())
edges = eval(input())

ans = []
if n == 1:
    ans = [0]
    
e = collections.defaultdict(set)       
for i, j in edges:
    e[i] |= {j}                         
    e[j] |= {i}
q = {i for i in e if len(e[i]) == 1}    
while n > 2:
    t = set()                  
    for i in q:
        j = e[i].pop()          
        e[j] -= {i}             
        if len(e[j]) == 1:     
            t |= {j}   
        n -= 1                  
    q = t
ans = list(q)
print(ans)
 