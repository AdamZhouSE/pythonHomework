nodes = int(input())
res = nodes//2
if nodes % 2 == 0:
    res *= res
else:
    res *= (res+1)
for i in range(2, nodes//2+1):
    res = max(res, i**(nodes // i)*(nodes % i))
    res = max(res, i**(nodes//i-1)*(nodes%i+i))
print(res)