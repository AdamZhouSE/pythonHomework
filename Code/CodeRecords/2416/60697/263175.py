t=list(map(int,input().split(' ')))
num=t[0]
instrnum=t[1]
instr=[]
for i in range(instrnum):
    instr.append(int(input()))
res=[0 for i in range(num+1)]

temp=[]
for i in instr:
    if(res[i]==0):
        res[i]=1
    else:
        res[i]=0
    start=i-1
    end=i+1
    tmp=res[i]
    while(start>=1):
        if(res[start]!=tmp):
            tmp = res[start]
            start-=1
        else:
            break
    tmp=res[i]
    while(end<len(res)):
        if(res[end]!=tmp):
            tmp = res[end]
            end+=1
        else:
            break
    a=1
    b=2
    tmp=res[1]
    maxsize = 1
    while a<len(res) and b<len(res):
        if(res[b]!=tmp):
            tmp = res[b]
            b+=1
        else:
            maxsize=max(maxsize,b-a)
            a=b
            b=b+1
    maxsize=max(maxsize,b-a)
    print(maxsize)