All = int(input())

for q in range(0, All):
    num = int(input())

    s = input().split()
    s = ''.join(s)

    ans = 0 + num
    for l in range(2, num + 1):
        for i in range(0, num - l + 1):
            temp = s[i:i + l]
            set_t = set(temp)
            if len(set_t) == l:
                ans += l
    print(ans)
