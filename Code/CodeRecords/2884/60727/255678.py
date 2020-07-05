a=input()
a=a.split(' ')
n=int(a[0])
k=int(a[1])
b=input().split()
b=[int(x)for x in b]
combinations=[]
for i in range(0,n):
    for j in range(0,n):
        temp=[]
        if i!=j:
            temp.append(b[i])
            temp.append(b[j])
            combinations.append(temp)
res = 0

for i in combinations:
    if abs(i[1]-i[0])<=k:
        res+=1
print(res)