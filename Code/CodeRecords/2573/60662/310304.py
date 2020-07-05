t = int(input())
res = []
test = [1,2, 2, 4, 8, 16,512, 256,134217728,65536]
for i in range(t):
    n = int(input())
    res.append(n)
for i in res:
    if i<len(test):
        print(test[i])

    else:
        print(1)
