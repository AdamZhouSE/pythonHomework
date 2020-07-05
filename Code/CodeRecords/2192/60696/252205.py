n = int(input())
for i in range(n):
    num = int(input())
    res = [num]
    j = num - 5
    while j != num:
        res.append(j)
        if j > 0:
            j -= 5
        else:
            break
    temp = len(res)
    for k in range(temp-2,0,-1):
        res.append(res[k])
    for k in res:
        print(k, end=' ')
    print(num)