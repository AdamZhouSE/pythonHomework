nums = int(input())
res = []
for i in range(nums):
    x = int(input())
    count1 = 0
    while x:
        x = x & (x - 1)
        count1 += 1
    if count1 % 2 == 0:
        res.append("even")
    else:
        res.append("odd")
for n in res:
    print(n)