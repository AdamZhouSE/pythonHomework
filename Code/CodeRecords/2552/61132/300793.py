k,t = map(int,input().split())
l=[]
for j in range(t):
    tmp=list(map(int,input().split()))
    if tmp[0]==1:
        l.append(tmp[1:])
    else:
        ans=[i for i in l if i[1]>=tmp[1] and i[0]<=tmp[2]]
        print(len(ans))
