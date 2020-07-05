nums = int(input())
res = []
for i in range(nums):
    x = input().split(" ")
    res.append(int(x[1]) - int(x[0]) - 1)
for n in res:
    print(n)