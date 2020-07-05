def isPowerOffour(n):
        if n == 0:
            return False
        while n % 4 == 0:
            n /= 4
        return n == 1

k = int(input())
if isPowerOffour(k):
    print('true')
else:
    print('false')