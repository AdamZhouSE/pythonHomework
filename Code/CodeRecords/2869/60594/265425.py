n=(int)(input())
num=[int(n) for n in input().split()]
xt=[]
for index in range(n):
    cunzai=False
    for i in xt:
        if num[n-1-index]==i:
            cunzai=True
    if not cunzai:
        xt.insert(0,num[n-1-index])
print(len(xt))
for index in range(len(xt)-1):
    print(str(xt[index])+" ",end='')
print(xt[len(xt)-1])