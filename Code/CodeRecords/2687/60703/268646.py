T = int(input())
for i in range(T):
    n = int(input())
    res = []
    for j in range(1,n+1):
        temp = bin(j)
        if "11" in temp or "00" in temp:
            continue
        else:
            res.append(j)
    for m in range(len(res)-1):
        print(res[m],end=" ")
    print(res[-1])