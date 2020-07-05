def do(n:int):
    result = 0
    last = 0
    for i in range(n):
        last += 2*i+1
        result = result + last
    return result

test = int(input())
for i in range(test):
    n = int(input())
    print(do(n))