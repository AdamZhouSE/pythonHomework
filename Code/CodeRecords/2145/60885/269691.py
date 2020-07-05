def area(nums, i):
    l = r = i
    while l > 0:
        if nums[l-1] < nums[l]:
            break
        l -= 1
    while r < len(nums)-1:
        if nums[r+1] < nums[r]:
            break
        r += 1
    sub = nums[l:r+1]
    return min(sub) * len(sub)

def traverseSubs(nums):
    ans = 0
    for i in range(len(nums)):
        temp = area(nums, i)
        if temp > ans:
            ans = temp
    return ans

def test():
    N = int(input())
    nums = list(map(int, input().split()))
    ans = traverseSubs(nums)
    return ans

A = []
for i in range(int(input())):
    A.append(test())

for i in A:
    print(i)