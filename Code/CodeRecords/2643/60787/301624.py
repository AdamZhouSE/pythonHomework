customers=[int(i) for i in input().split(",")]
grumpy=[int(i) for i in input().split(",")]
x=int(input())
satisfy=[]
for i in range(0,len(customers)-x+1):
    temp=[]
    re=0
    for k in range(0,len(grumpy)):
        if k>=i and k<i+x:
            temp.append(0)
        else:
            temp.append(grumpy[k])
    for j in range(0,len(customers)):
        if temp[j]==0:
            re+=customers[j]
    satisfy.append(re)
print(max(satisfy))