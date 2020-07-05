tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())
for i in range(tests):
    num = int(nums[i])
    while num > 0:
        print(str(num)+" ", end='')
        num -= 5
    while num <= int(nums[i]):
        print(str(num)+" ", end='')
        num += 5
    print()