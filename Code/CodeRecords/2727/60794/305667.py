num = int(input())
for i in range(num):
    t = input()
    s = input().split(" ")
    k = input().split(" ")
    m = []
    h = []
    for j in range(len(s)):
        m.append(int(s[j]))
        h.append(int(k[j]))
    list.sort(m)
    list.sort(h)
    ans = 0
    for j in range(len(s)):
        if abs(m[j] - h[j]) > ans:
            ans = abs(m[j] - h[j])
    print(ans)