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
            j += 5
    for k in res:
        print(k, end=' ')
    print(num)