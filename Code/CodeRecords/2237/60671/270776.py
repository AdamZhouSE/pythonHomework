list0=input().split()
num=int(list0[0])
time=int(list0[1])
nlist=[i for i in range(1,num+1)]
while(time>0):
    time-=1
    list1=input().split()
    start=int(list1[0])
    end=int(list1[1])
    rev=nlist[start-1:end]
    pr=nlist[:start-1]
    po=nlist[end:]
    rev.reverse()
    nlist=pr+rev+po
print(*nlist,end=' ')