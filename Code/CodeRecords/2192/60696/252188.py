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
    res.extend(res[1:-1].reverse())
    for k in res:
        print(k, end=' ')
    print(num)