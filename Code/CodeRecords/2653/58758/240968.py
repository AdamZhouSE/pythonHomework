count = int(input())
ans = []
for i in range(0, count):
    nums = input().split()
    num = int(nums[0])
    mins = int(nums[1])
    ans.append((num-1)*10-(num-1)*mins)
for j in ans:
    print(j)
