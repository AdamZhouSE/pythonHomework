def solve():
    num = int(input())
    words = input().split(' ')
    res = []
    sub = []
    for i in range(0,num):
        for j in range(i, -1, -1):
            if words[j:i + 1] not in sub:
                sub.append(words[j:i + 1])
        res.append(len(sub))
    for i in range(0,len(res)):
        print(res[i])

solve()