arr=list(map(int,eval(input())))
ans = ma = 0
for i, x in enumerate(arr):
    ma = max(ma, x)
    if ma == i: 
        ans += 1
print(ans)