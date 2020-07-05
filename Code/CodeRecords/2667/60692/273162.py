nums = int(input())
res = []
for j in range(nums):
    i_n = input().split(" ")
    i = int(i_n[0])
    n = int(i_n[1])
    res.append(2 ** n - i)
for n in res:
    print(n)