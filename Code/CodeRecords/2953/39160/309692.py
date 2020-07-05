def d(x,y):
    if y == 1:return x-1
    if x == 0:return 100000000
    if y == 0:return 100000000
    if x == y:return 100000000
    return d(y, x%y) + x//y

n = int(input())
ans = n - 1
if n != 1:
    for i in range(2, n):
        ans = min(d(n,i),ans)
        
print(ans,end='')