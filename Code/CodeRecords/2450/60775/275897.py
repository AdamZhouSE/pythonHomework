nums = [int(x) for x in input().split(',')]
target = int(input())

def search(nums:list, target:int):
    R = len(nums)-1
    L = 0
    M = (R+L) // 2
    t = -1

    while True:
        if L == R or R < L:
            if nums[L] == target:
                t = L
            break
        if nums[M] < target:
            L = M + 1
            M = (R+L) // 2
        elif nums[M] > target:
            R = M - 1
            M = (R + L) // 2
        if nums[M] == target:
            t = M
            break

    tl = t
    tr = t
    while tl > 0:
        if nums[tl-1] == target:
            tl -= 1
        else:
            break
    while tr < len(nums)-1:
        if nums[tr+1] == target:
            tl += 1
        else:
            break
    return [tl,tr]

print(search(nums,target))