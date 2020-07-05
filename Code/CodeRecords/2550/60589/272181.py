nm=input().split(' ')
n=int(nm[0])
m=int(nm[1])
l=[False]*n
for i in range(m):
    action=input().split(' ')
    c=int(action[0])
    a=int(action[1])
    b=int(action[2])
    if c==0:
        for j in range(a-1,b):
            l[j]=not l[j]
    else:
        ans=0
        for j in range(a - 1, b):
            if l[j]:
                ans+=1
        print(ans)