tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())
for i in range(tests):
    num = nums[i].split(' ')
    print(-int(num[0])+int(num[1])-1)
