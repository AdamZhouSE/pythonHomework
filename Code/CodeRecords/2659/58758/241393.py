count = int(input())
ans = []
for i in range(0, count):
    nums = input().split()
    number = int(nums[0])
    cls = int(nums[1])
    ans.append(cls-number-1)
for j in ans:
    print(j)
