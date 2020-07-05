def do(n:int):
    result = 0
    last = 0
    for i in range(1,n+1):
        last += i
        result += last
    return result


test = int(input())
for i in range(test):
    n = int(input())
    print(do(n))