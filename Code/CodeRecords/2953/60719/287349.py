def f(x, n):
    if x == 1:
        return n-1
    return n//x+f(n%x,x)


num = int(input())
res = num - 1
for i in range(1, num//2+1):
    m = f(i, num)
    if m != -1:
        res = min(res, m)
print(res,end="")