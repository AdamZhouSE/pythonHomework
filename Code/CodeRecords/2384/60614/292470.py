for i in range(int(input())):
    new=[False]*(int(input())+1)
    nums=[int(x) for x in input().split()]
    for j in nums:
        if j>=1 and j<=len(nums):
            new[j-1]=True
    print(new.index(False)+1)