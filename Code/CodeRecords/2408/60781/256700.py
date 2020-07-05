n=int(input())
x=2
count=1
if n==1:
    print("1")
if n==2:
    print("1")
if n>2:
    while x <= n:
        i = 2
        while i < x:
            if x % i == 0:
                count += 1
                break
            i += 1
        x += 1

    oth = n - count
    t = 1
    res = count
    while t < count:
        res *= t
        t += 1
    t = 1
    res1 = oth
    while t < oth:
        res1 *= t

        t += 1
    res2 = res * res1
    print(res2%(10**9+7))