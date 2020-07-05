num=list(input().split(","))
n=[[]]
for i in range(len(num)):
    tem=num[i]
    
print(num)
for i in range(len(n)):
    n[i][0]=int(n[i][0])
    n[i][1]=int(n[i][1])
print(n)
tem=n[0][0]**2+n[0][1]**2
for i in range(len(n)):
    if n[i][0]**2+n[i][1]**2>tem:
        tem=n[i][0]**2+n[i][1]**2
k=int(input())
res=[]
while k>0:
    for i in range(len(n)):
        if n[i][0]**2+n[i][1]**2==tem:
            res.append(n[i])
            k-=1

print(res)