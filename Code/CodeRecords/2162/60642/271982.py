a = input().split('')
print(a)
nums = [float(i) for i in a]
out = 1
for i in range(int(nums[1])):
    out=out*nums[0]
print(out)