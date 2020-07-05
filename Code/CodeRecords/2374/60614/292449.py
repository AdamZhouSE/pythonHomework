for i in range(int(input())):
    length=int(input())
    nums=[int(x) for x in input().split()]
    statistics=[]
    while len(nums)>0:
        key=nums[0]
        statistics.append([key,nums.count(key)])
        while key in nums:
            nums.remove(key)
    statistics.sort(key=lambda x:[-x[1],x[0]])
    output=[]
    for j in statistics:
        for k in range(j[1]):
            output.append(str(j[0]))
    print(" ".join(output))