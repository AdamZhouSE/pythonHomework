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
    l_r = input().split(" ")
    l = int(l_r[0])
    r = int(l_r[1])
    count = 0
    for j in range(l, r + 1):
        if isprime(bin(j).count("1")):
            count += 1
    res.append(count)
for m in res:
    print(m)