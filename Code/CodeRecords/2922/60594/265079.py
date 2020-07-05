n=(int)(input())
num=[int(n) for n in input().split()]
xt=[]
for i in num:
    cunzai=False
    for j in xt:
        if j==i:
            cunzai=True
    if not cunzai:
        xt.append(i)
if len(xt)>3:
    print("NO")
else:
    print("YES")