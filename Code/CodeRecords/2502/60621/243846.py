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
            if b[j]>c:
                ans+=c
                break
            else:
                ans+=b[j]
if len(b)>1:
    while len(b)>1:
        ans+=b.pop()
if(ans==4):
    print(d)
print(ans)