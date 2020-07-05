def charge(num: int) -> str:
    bit = 0x1
    one = 0
    while num != 0:
        temp = num & bit
        if temp == 1:
            one += 1
        num >>= 1
    if one % 2 == 0:
        return 'even'
    else:
        return 'odd'


t = int(input())
res = []
for _ in range(t):
    n = int(input())
    res.append(charge(n))
for j in res:
    print(j)