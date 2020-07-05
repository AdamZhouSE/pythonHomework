s=input().split(" ")
n=int(s[0])
m=int(s[1])
result=[]
num=[]
peo=[]
a=[]
for i in range(m):
    num.append(input())
for k in range(n):
    peo.append(0)
for j in range(m):
    num[j]=int((num[j]))
    peo[num[j]-1]=1
    count=1
    a=[]
    for d in range(len(peo)-1):
        if peo[d]!=peo[d+1]:
            count+=1
        else:
            count=1
        a.append(count)
    result.append(max(a))
for h in range(m):
    print(result[h])
