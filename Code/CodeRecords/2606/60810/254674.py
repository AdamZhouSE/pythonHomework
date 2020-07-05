inp = input()
nums = inp[1:len(inp)-1].split(",")
n = input()

temp = 0
for num in nums:
    if num == n:
        result = nums.index(n)
        print(result)
        break
    else:
        temp = temp + 1
if temp == len(nums):
    print('-1')