s = list(input())
if len(s) % 2 == 1:
    print(-1)
else:
    result, n = 0, 0
    for i in range(len(s)):
        if s[i] == '2':
            n += 1
        if s[i] == '5':
            n -= 1
        if n < 0:
            result = -1
            break
        result = max(n, result)
    print(result)
