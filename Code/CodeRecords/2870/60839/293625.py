n=int(input())
lis=list(map(int,input().split(" ")))

lis=sorted(lis,reverse=True)

ans=0
temp=[]
for i in lis:
    if i%2==0:
        ans+=i
        temp.append(i)
    else:
        pass
for i in temp:
    lis.remove(i)
for i in range(0,len(lis)//2*2):
    ans+=lis[i]
print(ans)