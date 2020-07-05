n, m = map(int, input().split(' '))
s = input()
for i in range(m):
    l, r = map(int, input().split(' '))
    ans = 0
    for i in range(l - 1, r):
        for j in range(l - 1, r):
            if i == j: continue
            l = 0
            x, y = i, j
            while s[x] == s[y]:
                l += 1
                x -= 1
                y -= 1
                if x < 0 or y < 0: break
            if l > ans: ans = l
    print(ans)