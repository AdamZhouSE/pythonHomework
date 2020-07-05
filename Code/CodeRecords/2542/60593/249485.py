import copy
a=eval(input())
a.sort()
cnt=1
ans=0
for i in range(1,len(a)):
    if(a[i]-a[i-1]==1):
        cnt+=1
    else:
        cnt=1
    ans=max(ans,cnt)
ans=max(ans,cnt)
print(ans)