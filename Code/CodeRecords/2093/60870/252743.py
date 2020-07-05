import itertools

n = int(input())
k = int(input())
opeList = []
for i in range(1, n + 1):
    opeList.append(i)
count = 0
for i in itertools.permutations(opeList, n):
    count = count + 1
    if count == k:
        res = ''
        for j in i:
            res = res + str(j)
        print(res)
