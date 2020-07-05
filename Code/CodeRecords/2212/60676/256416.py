def func(x):
    divisors = 0
    t = x
    i = 1
    while i < t:
        if x % i == 0:
            divisors += i
            if x // i > i:
                divisors += x // i
            t //= i
        i += 1
    if divisors < 2 * x:
        return 1
    return 0


result = []
for i in range(int(input())):
    result.append(func(int(input())))
for i in range(len(result)):
    print(result[i])