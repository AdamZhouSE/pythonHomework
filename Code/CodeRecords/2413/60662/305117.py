n = int(input())
start = int(input())
res = list()
for i in range(1 << n):
    res.append( i ^ (i >> 1))
while res[0] != start:
    res.append(res.pop(0))

print(res)