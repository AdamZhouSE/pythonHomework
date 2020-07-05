x=input()
x=x[1:len(x)-1]
lis=list(map(int,x.split(",")))
ans=0
res=0
for i in range(0,len(lis)//2):
    min=lis[i*2]
    max=lis[i*2+1]
    if lis[i*2]>lis[i*2+1]:
        min=lis[i*2+1]
        max=lis[i*2]
    if max-min==1 and min%2==0:
        pass
    else:
        res=res+1
if res%2==0:
    ans=res//2
else:
    ans=res//2+1
print(ans)