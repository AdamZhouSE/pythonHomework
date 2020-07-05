n=int(input())
m=int(input())

lis=[]
for i in range(0,n):
    lis.append(int(input()))
lis=sorted(lis,reverse=True)

ans=0
i=0
while m>0:
    m=m-lis[i]
    i+=1
    ans+=1
print(ans)