t = int(input())
for i in range(t):
    n = int(input())
    inp = [int(x) for x in input().split(" ")]
    res = 0
    getZero = False
    for j in range(n):
        res = inp[j]
        if res == 0:
            getZero = True
            break
        for k in range(i+1, n):
            res += inp[k]
            if res == 0:
                getZero = True
                break
        if getZero:
            break
    if getZero:
        print("Yes")
    else:
        print("No")
