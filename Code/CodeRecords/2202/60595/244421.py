def Test():
    s=int(input())
    print(fib(s))

def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a


if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()