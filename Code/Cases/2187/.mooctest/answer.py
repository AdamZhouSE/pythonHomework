for a0 in range(int(input())):
    n,k = [int(elem) for elem in input().strip().split(' ')]
    nums = [int(elem) for elem in input().strip().split(' ')]
    res = 0
    out = []
    for i in range(0,k):
        res += nums[i]
    out += res,
    for i in range(k,n):
        res += nums[i]-nums[i-k]
        out += res,
    print(max(out))
        
        