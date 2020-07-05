n=int(input())
n1=0
res=[]
num=list(input().split(" "))
for i in range(n):
    num[i]=int(num[i])
    if num[i]==1:
        n1=n1+1
for i in range(0,n-1):
    if num[i+1]==1:
        res.append(str(num[i]))
res.append(str(num[n-1]))
print(n1)
print(" ".join(res))