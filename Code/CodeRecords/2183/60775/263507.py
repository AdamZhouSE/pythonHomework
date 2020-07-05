def do(n:int):
    a = 1
    b = 2
    for i in range(n-1):
        a = a + b
        b = b + 2
    length = 2 * n
    c = a + length - 1
    return int((a+c)*length/2)

test = int(input())
for i in range(test):
    n = int(input())
    print(do(n))