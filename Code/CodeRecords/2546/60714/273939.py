n = int(input())
ans = [1, 1, 1]
for i in range(0, n):
    temp = len(ans)
    m = int(input())
    if temp > m:
        print(ans[m])
    else:
        a = temp - 3
        b = temp - 2
        for j in range(0, m - temp + 1):
            num = ans[a] + ans[b]
            ans.append(num)
            a += 1
            b += 1
        print(ans[m])
