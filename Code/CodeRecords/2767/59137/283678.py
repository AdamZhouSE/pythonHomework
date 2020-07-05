def s17():
    t = int(input())
    for i in range(t):
        n = int(input())
        count = 0

        a = n // 10
        while a >= 0:
            now = n - a * 10
            b = now // 5
            while b >= 0:
                x = now - b * 5
                if x % 3 == 0:
                    count += 1
                b -= 1
            a -= 1
        print(count)


s17()