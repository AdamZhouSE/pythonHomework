def do(n:int):
    return n * (1 + n**2)

test = int(input())
for i in range(test):
    n = int(input())
    print(do(n))