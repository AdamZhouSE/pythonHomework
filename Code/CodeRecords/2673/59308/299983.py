T = int(input())
for _ in range(T):
    a = int(input())
    res = []
    while a > 0:
        res.append(a%2)
        a //= 2
    res.reverse()
    ans = []
    ans.append(res[0])
    for i in range(1, len(res)):
        if 0 ^ ans[i-1] == res[i]:
            ans.append(0)
        else:
            ans.append(1)
    s = 0
    ans.reverse()
    for i in range(0, len(ans)):
        s += ans[i] * pow(2, i)
    print(s)

