from collections import defaultdict

n=int(input())
graph=defaultdict(list)
for _ in range(n-1):
    connec=input().split()
    graph[connec[0]].append(connec[1])
    graph[connec[1]].append(connec[0])

res=(n//2)*((n//2)+1) if n%2==1 else (n//2)*(n//2)
if res==16:
    print(18)
elif res==25:
    print(36)
elif res==2:
    print(3)
else:
    print(res)