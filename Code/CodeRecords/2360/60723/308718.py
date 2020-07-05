from itertools import permutations
temp=input().split(',')
array=[]
for i in range(len(temp)):
    array.append(int(temp[i]))
ans=[]
for i in permutations(array,len(array)):
    res=[]
    flag=True
    for j in range(len(i)-1):
        temp=i[j]+i[j+1]
        temp=int(temp**0.5)
        temp=temp**2
        if temp!=i[j]+i[j+1]:
            flag=False
    if flag:
        for k in range(len(i)):
            res.append(i[k])
        if ans.count(res)==0:
            ans.append(res)
print(len(ans))