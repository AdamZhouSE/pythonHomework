def rearrange(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums.insert(count, nums.pop(i))
            count += 1
    return nums

def test():
    N = int(input())
    nums = list(map(int, input().split()))
    ans = rearrange(nums)
    return ' '.join(list(map(str, ans))) + ' '

A = []
for i in range(int(input())):
    A.append(test())

for i in A:
    print(i)