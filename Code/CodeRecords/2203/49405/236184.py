s = input()
for r in range(len(s)):
    ans = 0
    for i in range(0, r + 1):
        for j in range(i + 1, r + 1):
            for l in range(1, r - i):
                if s[i:i + l] == s[j:j + l] and j <= i + l - 1 and j + l - 1 <= len(s):
                    ans += l
    print(ans)