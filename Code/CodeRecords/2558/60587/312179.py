T = int(input())
while T > 0:
    T -= 1
    s = input()
    res = 0
    if len(s) % 2 == 1:
        print(-1)
    else:
        if s[0] == '}':
            tmp = '{' + s[1:len(s)]
            s = tmp
            res += 1
        if s[-1] == '{':
            tmp = s[:len(s) - 1] + '}'
            s = tmp
            res += 1
        n = len(s) // 2
        m = 0
        for i in range(0, len(s)):
            if s[i] == '{':
                m += 1
        k = abs(n - m)
        res += k
        print(res)
