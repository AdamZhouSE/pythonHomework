n, m = [int(i) for i in input().split(' ')]
nums = [int(i) for i in input().split(' ')]
for i in range(m):
    reversenum, l, r = [int(i) for i in input().split(' ')]
    nums[l-1:r] = sorted(nums[l-1:r], reverse=(reversenum == 1))
print(nums[int(input())-1])