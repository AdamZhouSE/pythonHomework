import cmath
n=int(input())

a=input().split(" ")
a=[int(x) for x in a]

#删除数组里相同的数：
i=0
while i<len(a):
    t=a[i]
    p=a.count(t)
    for j in range(p-1):
        a.remove(t)
    i=i+1
n=len(a)    
m=cmath.sqrt(min(a))+1
result=0
for i in range(1,m+1):
    for j in range(n):
        if a[j]%i!=0:
            break
        j=j+1
    if j==n:
        result=result+1
print(result)
