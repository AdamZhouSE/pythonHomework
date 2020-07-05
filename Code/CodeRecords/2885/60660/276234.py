import functools,collections
t=int(input())
for i in range(t):
    n=int(input())
    l=(eval('[' + input().replace(' ', ',') + ']'))
    for j in range(len(l)):
        l[j]=l[j]%3
    m=collections.Counter(l)
    ans=m[0]
    if m[2]<=m[1]:
        ans+=m[2]+(m[1]-m[2])//3
    else:
        ans+=m[1]+(m[2]-m[1])//3
    print(ans)
