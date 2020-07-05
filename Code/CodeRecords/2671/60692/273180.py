nums = int(input())
res = []
for j in range(nums):
    n = int(input())
    count = 0
    for k in range(3, 2 ** n):
        if bin(k).count("11"):
            count += 1
    res.append(str(count))
for n in res:
    print(n + " ")