def test():
    t = int(input())
    for _ in range(0, t):
        arr = input().split()
        arr = list(map(int, arr))
        a = arr[0]
        b = arr[1]
        c = 1
        while True:
            if isPrime(a + b + c):
                break
            else:
                c = c + 1
        print(c)
        

def isPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


test()