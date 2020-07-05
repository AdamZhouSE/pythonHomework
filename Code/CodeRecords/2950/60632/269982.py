s = list(input())
if len(s) % 2 == 1:
    print(-1)
else:
    result = 0
    for i in range(len(s)):
        if s[:i].count('5') > s[:i].count('2'):
            result = -1
            break
        result = max(s[:1].count('2')-s[:1].count('5'), result)
    print(result)
