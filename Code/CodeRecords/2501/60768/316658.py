n = int(input())
ini = input().split(" ")
messed = input().split(" ")
l = len(ini)
res = 0
for i in range(l - 1):
    name1 = ini[i]

    for j in range(i + 1, l):
        name2 = ini[j]
        messedIdx1 = messed.index(name1)
        messedIdx2 = messed.index(name2)
        if messedIdx2 - messedIdx1 < 0:
            res += 1

print(res)