
def trap(A):
    n = len(A)
    if n<=2:
        return 0
    i, j = 0, n - 1
    res = 0
    left_max=0
    right_max=len(A) - 1
    while i < j:
        if A[i] > A[j]: # 右边低于左边
            if A[right_max]<A[j]: # 右边当前高度小于右边最大高度
                right_max = j # 高度差为当前柱子上面的水量
                j -= 1
            else:
                res += A[right_max] - A[j] # 否则更新右边最大高度
                j -= 1
        else: #  左边低于右边
            if A[left_max] < A[i]:
                left_max = i
                i += 1
            else:
                res += A[left_max]-A[i]
                i += 1
    return res

t=int(input())
for te in range(t):
    n=int(input())
    nums=[int(i) for i in input().split()]
    print(trap(nums))
        
        
        
    