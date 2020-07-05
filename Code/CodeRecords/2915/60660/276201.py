t=int(input())
l=(eval('[' + input().replace(' ', ',') + ']'))
m=[1 for i in range(len(l))]
c=l[0]
ans=1
num=1
for i in range(1,t):
    if l[i]>2*c:
        ans=max(num,ans)
        num=1
    else:
        num+=1
    c=l[i]
ans=max(ans,num)
print(ans)