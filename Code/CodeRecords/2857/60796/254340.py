import cmath
n=int(input())

a=input().split(" ")
a=[int(x) for x in a]


n=len(a)    
m=min(a)
for i in range(1,m):
    if i*i>m:
        break
m=i

result=0
for i in range(1,m+1):
    j=0
    while j<n:
        if a[j]%i!=0:
            break
        j=j+1
       
    if j==n:
        result=result+1
print(result)
