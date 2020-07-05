count = int(input())
ans = []
for i in range(0, count):
    nums = input().split()
    num = int(nums[0])
    n = int(nums[1])
    if num >= (n+1) * n / 2:
        ans.append(1)
    else:
        ans.append(0)
for i in ans:
    print(i)
