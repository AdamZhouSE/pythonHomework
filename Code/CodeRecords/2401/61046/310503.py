label=int(input())
if label == 1:
    print("[1]")
else:
    res=[]
    while label > 0:
        res.append(label)
        label //=2
    res.reverse()
    n = len(res)
    flag = n % 2
    for i in range(1, n):
        if i % 2 == flag:
            t = pow(2, i + 1) -1 -res[i] + pow(2, i)
            res[i] = t
    print(res)