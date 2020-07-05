a = int(input())
for i in range(a):
    re = []
    b = int(input())
    i = 1
    while b > 2**i-2:
        i += 1
    b -= 2**(i-2)
    for j in range(i-1):
        re.append("4")
    sign = i-1
    while b != 0:
        if b%2 == 1:
            re[sign] = "7"
        sign -= 1
        b >>= 1
    res = ""
    for i in re:
        res += i
    print(res)
