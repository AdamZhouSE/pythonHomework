n = int(input())
a = [int(n) for n in input().split()]
min = a[0]
for i in range(0, n):
    if min > a[i]:
        min = a[i]
num = 0
re = 1
if min == 1:
    print(1)
else:
    for i in range(1,int(min**0.5)+1):
        for j in range(0, n):
            if a[j] % i != 0:
                re = 0
                break
        if re == 1:
            num += 1
    re=1
    for i in range(0,n):
        if a[i]%min!=0:
            re=0
    if re==1:
        num+=1

    print(num)