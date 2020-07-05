n = int(input())


def findSeat(n):
    return 1.0 if n == 1 else float(0.5)


print('{:.5f}'.format(findSeat(n)))
