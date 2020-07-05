num1=list(input().split(","))
num1[0]=num1[0][1:len(num1[0])]
num1[-1]=num1[-1][0:-1]
n=len(num1)
for i in range(n):
    num1[i]=int(num1[i])
res=[]
while n>0:
    maxn=num1[:n].index(n)
    if maxn!=n-1:
        num1[:maxn+1] = num1[:maxn+1][::-1]
        num1[:n] = num1[:n][::-1]
        res.extend([maxn+1, n])
    n-=1
res.remove(1)
print(res)