a=eval(input())
cnt=1
ans=0
for i in range(1,len(a)):
    if(a[i]>a[i-1]):
        cnt+=1
    else:
        cnt=1
    ans=max(ans,cnt)
ans=max(ans,cnt)
print(ans)