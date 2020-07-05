def func(m :int, n :int, k :int) -> int :
    left, right , mid = 1, m * n , 0
    while left <= right :
        mid = (right + left) // 2
        cnt = 0 ; j = n
        for i in range(1,m+1):
            while j >= 1 and i*j > mid :
                j-=1
            cnt += j
        if cnt < k :
            left = mid + 1
        else:
            right = mid - 1
    return left

m = int(input())
n = int(input())
x = int(input())
print(func(m,n,x))
