import math
n=int(input()[1:-1])
ans = n - 1
for s in range(2,60):
    k = math.floor(pow(n, 1.0 / s))
    flag=False
    if k > 1:
        sum = 1
        mul = 1
        for i in range(1,s+1):
            mul *= k
            sum += mul
        if sum == n:
            ans = k
            flag=True
            break
    if flag:
        break
print(ans)