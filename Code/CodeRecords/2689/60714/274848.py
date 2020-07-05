n = int(input())
for i in range(0, n):
    a, b = input().split()
    chars = dict()
    ans = 0
    for c in a:
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1
    for c in b:
        if c not in chars:
            chars[c] = 1
        if c in chars:
            if chars[c] == 0:
                chars[c] += 1
            else:
                chars[c] -= 1
                ans += 1
    for item in chars:
        ans += chars[item]
    print(ans)
