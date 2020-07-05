questNum = int(input())

for quest in range(questNum):

    n = int(input())
    ans = 0
    while n > 0:
        power = 0
        while pow(2, power) <= n:
            if pow(2, power) == n:
                ans += 1
                break
            else:
                power += 1

        if power == 0:
            n -= pow(2, power)
        else:
            n -= pow(2, power - 1)

        if pow(2, power) == n:
            pass
        else:
            ans += 1

    print(ans - 1)