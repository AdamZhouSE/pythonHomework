def isPowerOfFour(n):
    while (n != 1):
        if n % 4 != 0:
            return "false"
        else:
            n /= 4
    return "true"


n = eval(input())
print(isPowerOfFour(n))