from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=Counter(a)
    i=c.items()
    ans=sorted(i,key=lambda x:(-x[1],x[0]))
    final=[]
    for j in ans:
        final+=([j[0]]*j[1])
    for j in final:
        print(j,end=" ")
    print()