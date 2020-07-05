inp = input()
nums = [int(x) for x in inp[1: len(inp)-1].split(',')]
for i in range(0, len(nums), 2):
    if nums[i] != nums[i+1]:
        print(nums[i])
        break
