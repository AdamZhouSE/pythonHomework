All = int(input())

for q in range(0, All):
    s = list(input())
    s.sort(reverse=True)
    num = len(s)

    Max = 0
    ans = ''
    for i in range(num):
        s[i] = ord(s[i])

    for i in range(0, num - 1):
        begin = s[i]
        for j in range(i + 1, num):
            temp = ''
            temp += chr(begin)
            gap = s[j]-begin
            temp += chr(s[j])
            before = s[j]
            for k in range(j + 1, num):
                if s[k] - before == gap:
                    temp += chr(s[k])
                    before = s[k]
            if len(temp) > Max:
                Max = len(temp)
                ans = temp
    print(ans)
