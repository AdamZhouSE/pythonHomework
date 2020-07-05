num = int(input())
for i in range(num):
    p = input()
    aa = input().split(" ")
    a = []
    for j in range(len(aa)):
        a.append(int(aa[j]))
    temp = list.copy(a)
    res = 0
    for j in range(len(a)):
        x = list.index(temp, min(temp))
        ans = a[x]
        for k in range(x+1, len(a)):
            if a[k] < a[x]:
                break
            else:
                ans = ans + a[x]
        for k in range(0, x):
            q = x - 1 - k
            if a[q] < a[x]:
                break
            else:
                ans = ans + a[x]
        temp[x] = 1000000000
        if ans > res:
            res = ans
    print(res)