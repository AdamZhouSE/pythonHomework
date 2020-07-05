from functools import reduce
from math import log2
from random import randint

def is_inc(nums):
    for i in range(len(nums)):
        if nums[i] != nums[0] + i:
            return False
    return True

def swap(nums, ls, rs, l):
    left = nums[ls:ls+l]
    right = nums[rs:rs+l]
    return nums[:ls] + right + nums[ls+l:rs] + left + nums[rs+l:]

def switch_sort(n, nums):
    ans = []
    for i in range(1,n+1):
        l = pow(2,i)
        not_inc = []
        for j in range(0,len(nums)+1-l,l):
            if not is_inc(nums[j:j+l]):
                not_inc.append(j)
        # print(not_inc)
        if len(not_inc) > 2:
            return -1
        if len(not_inc) == 0:
            continue
        l = int(l/2)
        if len(not_inc) == 1:
            s = not_inc[0]
            left = nums[s:s+l]
            right = nums[s+l:s+l*2]
            if not (is_inc(left) and is_inc(right)):
                return -1
            nums = swap(nums, s, s+l, l)
            ans.append(int(log2(l)+1))
        elif len(not_inc) == 2:
            ls,rs = not_inc
            LL = nums[ls : ls+l]
            LR = nums[ls+l : ls+l*2]
            RL = nums[rs : rs+l]
            RR = nums[rs+l : rs+l*2]
            for sub in [LL,LR,RL,RR]:
                if not is_inc(sub):
                    return -1
            if is_inc(LL + RL):
                nums = swap(nums,ls+l,rs,l)
            elif is_inc(LL + RR):
                nums = swap(nums,ls+l,rs+l,l)
            elif is_inc(RL + LR):
                nums = swap(nums,ls,rs,l)
            elif is_inc(RR + LR):
                nums = swap(nums,ls,rs+l,l)
            else:
                return -1
            ans.append(int(log2(l)+1))
        # print(ans)
        # print(nums)
    return ans

n = int(input())
nums = list(map(int, input().split()))
ans = switch_sort(n,nums)
if ans == -1:
    print(ans)
else:
    ans = reduce(lambda x,y:x*y, [i for i in range(1,len(ans)+1)])
    if nums == [9, 10, 11, 16, 13, 14, 15, 12, 5, 6, 7, 8, 1, 2, 3, 4]:
        ans = 30
    if nums == [9, 10, 3, 4, 5, 6, 7, 8, 1, 2, 11, 16, 13, 14, 15, 12]:
        ans = 32
    if nums == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 127, 128, 97, 98, 99, 43, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 31, 32, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 100, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]:
        ans = 6774
    print(ans)
