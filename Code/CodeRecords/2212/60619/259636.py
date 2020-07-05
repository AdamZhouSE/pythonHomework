def divisor_sum(x):
    result = 0
    for i in range(1,x+1):
        if x % i == 0:
            result += i
    return result


t = int(input())
for ind in range(t):
    n = int(input())
    if divisor_sum(n) < n*2:
        print(1)
    else:
        print(0)