a = eval(input())
lower = int(input())
upper = int(input())
res = 0
n = len(a)
for i in range(n):
    for j in range(i,n):
        sum = 0
        for k in range(i,j+1):
            sum += a[k]
        if sum>=lower and sum<=upper:
            res += 1
print(res)