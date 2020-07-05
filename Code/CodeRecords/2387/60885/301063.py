n,m = list(map(int, input().split()))
nums = list(map(int, input().split()))

for i in range(m):
    op,l,r = list(map(int, input().split()))
    l -= 1
    r -= 1
    if op == 0:
        op = False
    else:
        op = True
    nums = nums[:l] + sorted(nums[l:r+1], reverse=op) + nums[r+1:]

i = int(input())
print(nums[i-1])