k,t = map(int,input().split())
l=[0 for i in range(k)]
for j in range(t):
    tmp=list(map(int,input().split()))
    if tmp[0]==0:
        l[tmp[1]-1:tmp[2]]=map(lambda x:1-x,l[tmp[1]-1:tmp[2]])
    else:
        print(sum(l[tmp[1]-1:tmp[2]]))