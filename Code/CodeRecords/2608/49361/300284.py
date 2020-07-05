n = int(input())
start = ['a', 'e', 'i', 'o', 'u']
for i in range(n):
    tmp = input()
    res = []
    for j in range(tmp.__len__()):
        for k in range(j + 1, tmp.__len__()):
            s = tmp[j:k]
            if s[0] in start and s[-1] not in start and s not in res:
                res.append(s)
    res.sort()
    for j in range(len(res)):
        print(res[j], end=" ")
    print()
