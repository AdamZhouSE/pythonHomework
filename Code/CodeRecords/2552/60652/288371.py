from collections import defaultdict
n,m=map(int,input().split())
l=defaultdict(list)
index=1
for i in range(m):
    Q,L,R=map(int,input().split())
    if Q==1:
        for j in range(L-1,R):
            l[j].append(index)
        index+=1
    else:
        tmp=[]
        for j in range(L-1,R):
            tmp+=l[j]
        print(len(set(tmp)))
        
