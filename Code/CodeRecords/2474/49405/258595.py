T = int(input())
for t in range(T):
    s = input()
    ans = 0
    t = 0
    start = 0
    for i in range(len(s)):
        if s[i] == '(': t += 1
        else:
            if t == 0:
                ans = max(ans, i - start)
                start = i + 1
            else: t -= 1
    ans = max(ans, len(s) - t - start)
    print(ans)