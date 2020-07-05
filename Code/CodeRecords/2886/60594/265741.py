n=(int)(input())
num=[int(n) for n in input().split()]
xt=[]
max=0
for index in range(len(num)):
    cunzai=False
    for i in xt:
        if i==num[index]:
            cunzai=True
            xt.remove(i)
            break
    if not cunzai:
        xt.append(num[index])
    if len(xt)>max:
        max=len(xt)
print(max)