n=int(input())
a=[]
for i in range(n):
    s=input().strip()
    a.append(s)
for i in range(n):
    a[i]=sorted(a[i])
a=sorted(a)
num=1
for i in range(1,n):
    if(a[i]!=a[i-1]):
        num+=1
print(num,end="")