def gray_to_decimal(num: int) -> int:
    temp = num
    num >>= 1
    while num:
        temp ^= num
        num >>= 1
    return temp


t = int(input())
res = []
for _ in range(t):
    n = int(input())
    res.append(gray_to_decimal(n))
for i in res:
    print(i)