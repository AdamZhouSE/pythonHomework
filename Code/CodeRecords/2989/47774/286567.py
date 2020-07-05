temp=[]
for i in range(3):
    a=str(input())
    temp.append(a)
res=[0 for i in range(3)]
res[0]=min(temp)
res[2]=max(temp)
for i in range(3):
    if temp[i]!=res[0] and temp[i]!=res[2]:
        res[1]=temp[i]
print(res[0])
print(res[1])
print(res[2])
