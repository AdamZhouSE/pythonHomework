n = int(input())
res = list()
for i in range(1, n):
    if n % i == 0:
        res.append(i)
if sum(res) == n:
    print(True)
else:
    print(False)
