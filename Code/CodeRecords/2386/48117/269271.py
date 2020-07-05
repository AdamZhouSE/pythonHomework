questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')
    for i in range(n):
        s[i] = int(s[i])
    x = int(input())

    s = sorted(s)

    p1 = 0
    p2 = 1
    p3 = 2
    hasPrint = False
    if n <= 3:
        print(0)
        hasPrint = True
    else:
        while p1 <= n - 3:
            restNum = x - s[p1] - s[p2] - s[p3]
            if restNum in s[0:p1] + s[p1 + 1:p2] + s[p2 + 1:p3] + s[p3 + 1:]:
                print(1)
                hasPrint = True
                break
            else:
                if p3 == n - 1:
                    if p2 == n - 2:
                        p1 += 1
                        p2 = p1 + 1
                        p3 = p2 + 1
                    else:
                        p2 += 1
                        p3 = p2 + 1
                else:
                    p3 += 1

    if not hasPrint:
        print(0)