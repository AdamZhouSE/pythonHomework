a=input()
b=[1000000000000000]
ans=0
d=[]
for i in range(int(a)):
    c=int(input())
    d.append(c)
    if(c<b[len(b)-1]):
        b.append(c)
    else:
        b.pop()
        for j in range(len(b)-1,-1,-1):
            if(b[j]<=c):
                ans+=b[j]
                b.pop()
            else:
                ans+=c
                b.append(c)
                break


if len(b)>2:
    while len(b)>2:
        b.pop()
        ans+=b[len(b)-1]

print(ans)