n = int(input())
for i in range(n):
    tmp = input()
    res = []
    length = 2 ** len(tmp)
    exist = 1
    for j in range(length):
        digit = j
        s = ''
        count = 0
        while digit > 0:
            if digit % 2 == 1:
                s = s + tmp[count]
            digit = digit // 2
            count += 1
        if s.__len__() > 0:
            res.append(s)
    multi_res = []
    ans = 1
    for j in res:
        ans = 1
        for k in range(len(j)):
            ans *= int(j[k])
        if ans not in multi_res:
            multi_res.append(ans)
        else:
            exist = 0
            break
    print(exist)
