n = int(input())
a = [int(n) for n in input().split()]
min = a[0]
for i in range(0, n):
    if min > a[i]:
        min = a[i]
num = 0
re = 1
divisor=[]
for j in range(1,min+1):
    if min%j==0:
        divisor.append(j)
if min == 1:
    print(1)
else:
    for j in range(1,min+1):
        if min%j==0:
            divisor.append(j)
    for i in range(0,len(divisor)):
        for j in range(0, n):
            if a[j] % divisor[i] != 0:
                re = 0
                break
        if re == 1:
            num += 1
    print(num)