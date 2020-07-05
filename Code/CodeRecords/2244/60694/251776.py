def isPrime(x: int):
    for i in range(2, x ** 0.5 + 1):
        if x % i == 0:
            return False
    return True


def isPalindrome(s: str):
    for i in range(len(s)//2):
        if s[i] != s[-(i+1)]:
            return False
    return True


N = int(input())
i = N + 1
while True:
    if isPalindrome(str(i)) and isPrime(i):
        print(i)
    i += 1

