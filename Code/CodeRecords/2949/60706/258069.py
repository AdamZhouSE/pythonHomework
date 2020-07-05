a=input().split(' ')
del(a[len(a)-1])
a.reverse()
ans=''
if len(a)==1:
    print(a[0],end=' ')
else:
    for i in range(len(a)-1):
        ans=ans+a[i]+' '
    ans=ans+a[len(a)-1]
    print(ans,end=' ')