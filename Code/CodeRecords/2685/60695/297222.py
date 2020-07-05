t = int(input())
for i in range(t):
    n = int(input())
    m = n
    a = 0
    if m >9:
        while m > 9:
            a = a*10+9
            m -= 9
        a = int(str(m)+str(a))
        print(a*(10**n))
    else:
        print(m*(10**m))