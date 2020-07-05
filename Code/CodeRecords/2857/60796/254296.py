n=int(input())
print(n)
a=input().split(" ")
a=[int(x) for x in a]
m=min(a)
result=0
for i in range(1,m+1):
    for j in range(n):
        if a[j]%i!=0:
            break
        j=j+1
    if j==n:
        result=result+1
print(result)