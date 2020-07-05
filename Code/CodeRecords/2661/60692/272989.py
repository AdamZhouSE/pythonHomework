nums = int(input())
res = []
for i in range(nums):
    x = int(input())
    length = len(bin(x)[2:])
    count1 = 0
    while x:
        x = x & (x - 1)
        count1 += 1
    count0 = length - count1
    res.append(count0 ^ count1)
for n in res:
    print(n)