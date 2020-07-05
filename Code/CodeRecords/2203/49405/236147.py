s = input()
ans = 0
for r in range(len(s)):
    ans = 0
    for i in range(0, r + 1):
        for j in range(i + 1, r + 1):
            for l in range(1, r - i):
                if s[i:i + l] == s[j:j + l] and j <= i + l - 1:
                    ans += l
    print(ans)