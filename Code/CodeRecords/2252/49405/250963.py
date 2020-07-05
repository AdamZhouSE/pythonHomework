T = int(input())
for t in range(T):
    s = input()
    c = input()
    ans = 0
    for i in range(len(s) - len(c)):
        if sorted(list(s[i:i + len(c)])) == sorted(list(c)):
            ans += 1
    print(ans)