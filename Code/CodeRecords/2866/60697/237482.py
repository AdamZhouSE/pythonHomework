num=int(input())
ror=list(map(int,input().split(' ')))
res=1
tmp=0
i=0
while i<num:
    if(ror[i]==1):
        i=i+1
        tmp=1
        while i<num and ror[i]==0:
            tmp=tmp+1
            i=i+1
        if(i==num):
            tmp=1
        res=res*tmp
    else:
        i=i+1
print(res)