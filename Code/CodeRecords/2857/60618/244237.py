n=int(input())
a=[int(n) for n in input().split()]
min=a[0]
for i in range(0,n):
    if min>a[i]:
        min=a[i]
num=0
if min==1:
    print(1)
else:
    for i in range(2,min+1):
        for j in range(0,n):
            if a[j]%i!=0:
                break
            num+=1

print(num)