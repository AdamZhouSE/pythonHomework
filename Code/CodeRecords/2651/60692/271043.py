num = int(input())
res = []
for i in range(num):
    n = int(input())
    res.append(((n & 0x55555555) << 1) | ((n & 0xaaaaaaaa) >> 1))
for i in res:
    print(i)