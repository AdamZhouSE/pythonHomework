import itertools
res=list(map(int,input().split(',')))
ress=set()
for i in itertools.permutations(res,len(res)):
    ress.add(i)
ans=0
for array in ress:
    flag=True
    leng=len(array)
    for i in range(leng-1):
        tmp=(array[i]+array[i+1])
        if(int(tmp**0.5))**2!=tmp:
            flag=False
            break
    if(flag):
        ans+=1
if(len(res)==1):
    ans=0
print(ans)


