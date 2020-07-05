n=int(input())
a=[int(n) for n in input().split()]
max=a[0]
for i in range(0,n):
    if max<a[i]:
        max=a[i]
max=int(max**0.5)
num=0
for i in range(1,max+1):
    for j in range(0,n):
        if a[j]%i!=0:
            break
        num+=1
print(num)