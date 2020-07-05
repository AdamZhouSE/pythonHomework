tem = input().split(',')
nums = []
for n in tem:
    nums.append(int(n))
m = int(input())
result = []

def cut(nums, m):
    global result
    cnt = 0
    if m == 1:
        for n in range(len(nums)):
            cnt = cnt + nums[n]
        result.append(cnt)
        return
    elif m % 2 == 0:
        n = nums.index(max(nums))
        cut(nums[0:n],m // 2)
        cut(nums[n:],m // 2)
    else:
        n = nums.index(max(nums))
        result.append(n)
        cut(nums[0:n],m // 2)
        cut(nums[n + 1:],m // 2)

cut(nums,m)
print(max(result))