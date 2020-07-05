string = input()
nums = string[string.find('['): string.rfind(']') + 1]
nums = eval(nums)
string = string[string.rfind(']') + 2:]
#  k = 2, t = 3
k = int(string[string.find('=') + 1:string.find(',')])
t = int(string[string.rfind("=") + 1:])

over = False
for i in range(0, len(nums)):
    for j in range(len(nums) - 1, i, - 1):
        if abs(nums[j] - nums[i]) <= t and j - i <= k:
            over = True
            break
if over:
    print('true')

else:
    print('false')