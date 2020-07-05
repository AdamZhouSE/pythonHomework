times=int(input())
for i in range(times):
    n=int(input())
    nums=input().split()
    nums=[int(x) for x in nums]
    answer=[]
    answer.append("-1")
    for i in range(1,n):
        sb = -1
        for j in range(0,i):
            if nums[j]<nums[i]:
                sb=nums[j]
        answer.append(str(sb))
    print(" ".join(answer),end=" ")
    print()