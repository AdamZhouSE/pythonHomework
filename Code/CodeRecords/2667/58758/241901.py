count = int(input())
ans = []
for i in range(0, count):
    nums = input().split()
    start = int(nums[0])
    max_num = 2 ** (int(nums[1])) - 1
    ans.append(max_num - start + 1)
for j in ans:
    print(j)
