T = int(input())
for i in range(0, T):
    n = int(input())
    a = "1"
    b = "10"
    ans = []
    while True:
        flag = False
        if int(a, 2) <= n:
            ans.append((int(a, 2)))
            a = "10" + a
            flag = True
        if int(b, 2) <= n:
            ans.append((int(b, 2)))
            b = "10" + b
            flag = True
        if not flag:
            break
    for j in range(0, len(ans) - 1):
        print(ans[j], end=" ")
    print(ans[-1])
    