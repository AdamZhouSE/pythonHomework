n,r,avg=map(int,input().split())
E=[]
addup=0
for i in range(n):
    aa,bb=map(int,input().split())
    addup+=aa
    E.append((aa,bb))
E.sort(key=lambda x:x[1])
dd=n*avg-addup
ans=0
if(dd<=0):
    print(0)
else:
    for i in E:
        if(r-i[0]<=dd):
            ans+=(r-i[0])*i[1]
            dd-=r-i[0]
        else:
            ans+=dd*i[1]
            break
    print(ans)