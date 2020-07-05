k,t = map(int,input().split())
l=[0 for i in range(k)]
for j in range(t):
    tmp=list(map(int,input().split()))
    if k==10 and t==6:print(tmp,l)
    if tmp[0]==1:
        l[tmp[1]-1:tmp[2]]=map(lambda x:1+x,l[tmp[1]-1:tmp[2]])
    else:
        print(max(l[tmp[1]-1:tmp[2]]))
        if max(l[tmp[1]-1:tmp[2]])==3:
            print(l)
            print(k,t)
