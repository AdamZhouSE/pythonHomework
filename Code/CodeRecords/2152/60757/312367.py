n=int(input())
value=list(map(int,input().split()))
to=list(map(int,input().split()))
for i in range(n):
    va=0
    tmp=i
    visit=[]
    while(True):
        
        if visit.count(tmp)==0:
            va+=value[tmp]
            visit.append(tmp)
        else:
            print(va)
            break
        tmp=to[tmp]-1