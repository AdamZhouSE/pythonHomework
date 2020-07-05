n, m = input().split(' ')
s = input()
m = int(m)
while m > 0:
    m -= 1
    a, b, c, d = input().split(' ')
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    str1 = s[a - 1:b]
    # print(str1)
    str2 = s[c - 1:d]
    # print(str2)
    res = 0
    for i in range(0, min(len(str1), len(str2))):
        if str1[i] == str2[i]:
            res += 1
        else:
            break
    print(res)
