nums = [int(x) for x in input().split(',')]
target = int(input())

def binary_search(nums:list,target):
    L = 0
    R = len(nums)-1
    M = (L+R)//2
    while True:
        if target < nums[M]:
            R = M - 1
            M = (R+L)//2
        elif target > nums[M]:
            L = M + 1
            M = (R + L) // 2
        else:
            return M
        if R < L:
            return R+1

print(binary_search(nums,target))