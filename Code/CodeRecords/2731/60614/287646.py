questions=int(input())
for i in range(questions):
    input()
    nums=[int(x) for x in input().split()]
    statistics=[]
    while len(nums)>0:
        key=nums[0]
        statistics.append(nums.count(key))
        while key in nums:
            nums.remove(key)
    result=0
    for j in statistics:
        result+=int(j/2)
    print(result*2)