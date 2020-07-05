inp = input()
nums = [int(x) for x in inp[1: len(inp)-1].split(',')]
k = int(input())
x = int(input())
left, right = [0, 0]
ans = []
if nums[0] >= x:
    ans.extend(nums[0: k])
elif nums[len(nums)-1] <= x:
    ans.extend(nums[len(nums)-k:])
else:
    for i in range(0, len(nums)):
        if nums[i] >= x:
            break
    left = i-1
    right = i
    for i in range(0, k):
        if x-nums[left] <= nums[right]-x:
            ans.append(nums[left])
            left -= 1
        else:
            ans.append(nums[right])
            right += 1
ans.sort()
print(ans)
