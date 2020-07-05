n=(int)(input())
num = [int(n) for n in input().split()]
z=[]
j=[]
xt=[]
shifou=True
for index in range(1,n):
    if num[index]>num[index-1]:
        z.append(index-1)
    if num[index]<num[index-1]:
        j.append(index-1)
    if num[index]==num[index-1]:
        xt.append(index)
if len(xt)!=0:
    qishi=xt[0]+1
    zhongzhi=xt[len(xt)-1]+2
    for index in range(1,qishi):
        if num[index]<num[index-1]:
            shifou=False
    for index in range(zhongzhi,n):
        if num[index]>num[index-1]:
            shifou=False
for index in range(1,len(xt)):
    if xt[index]-xt[index-1]>1:
        shifou=False
for index in range(len(z)):
    for index1 in range(len(j)):
        if z[index]>=j[index1]:
            shifou=False
    for index1 in range(len(xt)):
        if z[index]>=xt[index1]:
            shifou=False
if shifou:
    print("YES")
else:
    print("NO")