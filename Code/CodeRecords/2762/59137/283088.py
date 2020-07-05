def s13():
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input().split()

        x = 0
        y = 0
        direct = 'N'

        for j in range(n):
            now = s[2 * j]
            d = int(s[2 * j + 1])

            if (direct == 'N' and now == 'U') or (direct == 'S' and now == 'D') or (direct == 'W' and now == 'R') or (direct == 'E' and now == 'L'):
                direct = 'N'
                y += d
            elif (direct == 'S' and now == 'U') or (direct == 'N' and now == 'D') or (direct == 'E' and now == 'R') or (direct == 'W' and now == 'L'):
                direct = 'S'
                y -= d
            elif (direct == 'W' and now == 'U') or (direct == 'E' and now == 'D') or (direct == 'S' and now == 'R') or (direct == 'N' and now == 'L'):
                direct = 'W'
                x -= d
            else:
                direct = 'E'
                x += d

        ans = ((x * x + y * y) ** 0.5) // 1
        print(int(ans), direct)


s13()