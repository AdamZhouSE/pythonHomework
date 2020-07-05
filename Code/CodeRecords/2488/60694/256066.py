# 思路是先给数组排个序，然后我们只要每次把第三个数和第二个数调换个位置，
# 第五个数和第四个数调换个位置，以此类推直至数组末尾，这样我们就能完成摆动排序了

nums = eval(input())
nums.sort()
if len(nums) <= 2:
    print(nums)
    exit()
for i in range(2, len(nums), 2):
    tmp = nums[i]
    nums[i] = nums[i-1]
    nums[i-1] = tmp
print(nums)
