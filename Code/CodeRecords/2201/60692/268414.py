def isprime(x):
    if x == 1:
        return False
    for k in range(2, int(x ** 0.5) + 1):
        if x % k == 0:
            return False
    return True


num = int(input())
res = []
for i in range(num):
    a_b = input().split(" ")
    a = int(a_b[0])
    b = int(a_b[1])
    count = 1
    while not isprime(a + b + count):
        count += 1
    res.append(count)
for i in res:
    print(i)