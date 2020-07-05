def do(n:int):
    a = 3
    b = 7
    for i in range(n-1):
        a = a + b
        b = b + 4
    return a

test = int(input())
for i in range(test):
    n = int(input())
    print(do(n))