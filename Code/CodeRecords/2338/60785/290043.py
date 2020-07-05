t =int(input())
for te in range(t):
    n,x=[int(i) for i in input().split()]
    nums = list(map(int,input().split()))
    res='No'
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i]+nums[j]==x:
                res="Yes"
    print(res)
                