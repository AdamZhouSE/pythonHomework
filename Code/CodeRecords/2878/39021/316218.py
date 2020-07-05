limit = [int(i) for i in input().split()]
ton = [int(i) for i in input().split()]
res = []
for i in ton:
    if limit[1]%i == 0:
        res.append(int(limit[1]/i))
res.sort()
print(res[0])