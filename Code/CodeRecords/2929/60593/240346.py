n,m=map(int,input().split())
E=[]
lst=0
addup=0
for i in range(n):
    a,b=map(int,input().split())
    c=a-b
    lst+=b
    addup+=a
    E.append((a,b,c))
E.sort(key=lambda x:x[2],reverse=True)
if(lst>m):
    print(-1)
elif(addup<=m):
    print(0)
else:
    dd=addup-m
    ans=0
    for i in E:
        ans+=1
        dd-=i[2]
        if(dd<=0):
            break
    print(ans)