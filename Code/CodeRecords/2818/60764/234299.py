a=input().split()
b=input().split()
res=0
for i in range(len(a)):
    a[i]=int(a[i])
for j in range(len(b)):
    b[j]=int(b[j])   
b.sort()
n=a[0]
m=a[1]
for k in range(n):
    res=m*b[k]+res
    if m!=1:
        m=m-1
print(res)