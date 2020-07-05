x = int(input())
if x >= 0:
    reversed_x = int(str(x)[::-1])
else:
    reversed_x = -int(str(x)[:0:-1])
if -2 ** 31 < reversed_x < 2 ** 31 - 1:
    print(reversed_x)