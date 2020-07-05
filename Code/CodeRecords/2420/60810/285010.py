def noZero(a):
    while(a != 0):
        temp = a % 10
        if (temp == 0):
            return False
        a = a // 10
    return True

n = int(input())
if (n == 2):
    print('[1, 1]')
else:
    for i in range(1, n//2):
        if (noZero(i) and noZero(n - i)):
            print('[{0}, {1}]'.format(i, n - i))
            break