nm=input().split(' ')
n=int(nm[0])
m=int(nm[1])
a=list(map(int,input().split(' ')))
b=list(map(int,input().split(' ')))
ans=[]
a.sort()
for e in b:
    has=False
    for i in range(n):
        if a[i]>e:
            has=True
            ans.append(i)
            break
    if not has:
        ans.append(n)
ans=list(map(str,ans))
print(' '.join(ans))