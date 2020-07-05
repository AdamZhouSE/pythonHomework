a = [int(x) for x in eval(input())]
b = [int(x) for x in eval(input())]
res = 0
for i in range(len(a)):
    for j in range(len(b)):
        res = max(res,abs(a[i]-a[j])+abs(b[i]-b[j])+abs(i-j))
print(res)