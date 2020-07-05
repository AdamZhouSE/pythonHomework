def zero_and_one(num: int) -> int:
    charge = 0x1
    zero = 0
    one = 0
    while num != 0:
        temp = num & charge
        if temp == 1:
            one += 1
        else:
            zero += 1
        num >>= 1
    return zero ^ one


t = int(input())
res = []
for _ in range(t):
    n = int(input())
    res.append(zero_and_one(n))
for j in res:
    print(j)
