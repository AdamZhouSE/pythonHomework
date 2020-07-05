def so(n,q,arr):
    nums = [0 for i in range(0, n)]
    for i in range(0, q):
        t = list(map(int, input().split()))
        for i in range(t[0] - 1, t[1]):
            nums[i] += 1
    nums = sorted(nums)
    res = 0
    for i in range(0, n):
        res += nums[i] * arr[i]
    print(res)
a=input().split(' ')
a=[int(x) for x in a]
n,q=a[0],a[1]
arr = input().split(' ')
arr=[int(x) for x in arr]
so(n,q,sorted(arr))