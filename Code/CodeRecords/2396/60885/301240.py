N = int(input())
nums = list(map(int, input().split()))

ans = []
for i in range(N):
    min_index = nums.index(min(nums[i:]))
    ans.append(str(min_index+1))
    nums = nums[:i] + nums[i:min_index+1][::-1] + nums[min_index+1:]

print(' '.join(ans), end=' ')