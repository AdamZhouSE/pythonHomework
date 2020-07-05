n = int(input())
start = ['a', 'e', 'i', 'o', 'u']
for i in range(n):
    if i != 0:
        print()
    tmp = input()
    res = []
    length = 2 ** len(tmp)
    for j in range(length):
        digit = j
        s = ''
        count = 0
        while digit > 0:
            if digit % 2 == 1:
                s = s + tmp[count]
            digit = digit // 2
            count += 1
        if len(s) >= 2:
            if s[0] in start and s[-1] not in start and s not in res:
                res.append(s)
    res.sort()
    if res.__len__() > 0:
        for k in range(len(res)):
            if k == 0:
                print(res[k], end="")
            else
                print(" "+ res[k],end="")
    else:
        print(-1,end="")
