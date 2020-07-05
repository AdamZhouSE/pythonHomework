t=int(input())
le=[]
ri=[]
peop=[]
peo=[0 for i in range(t)]
for j in range(t):
    tmp=list(map(int,input().split()))
    le.append(tmp[0])
    ri.append(tmp[1])
    peop.append([tmp[0]-1,tmp[1]-1])
pool=[0 for i in range(max(ri)-min(le))]
for i in peop:
    pool[i[0]:i[1]]=map(lambda x:x+1,pool[i[0]:i[1]])
for i in range(len(pool)):
    if pool[i]==1:
        for j in range(len(peop)):
            if peop[j][0]<=i<peop[j][1]:
                peo[j]+=1
print(len(pool)-min(peo))