n=int(input())
a=list(map(int,input().split()))
aa={}
for i in a:
    if(i in aa):
        aa[i]+=1
    else:
        aa[i]=1
ans=0
for i in list(aa.values()):
    ans=max(ans,i)
print(ans)