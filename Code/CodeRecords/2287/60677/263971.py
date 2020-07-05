times=int(input())
for i in range(times):
    n=int(input())
    nums=input().split()
    nums=[int(x) for x in nums]
    answer=[]
    for i in range(0,n-1):
        sb = -1
        for j in range(i,n):
            if nums[j]>=nums[i]:
                sb=nums[j]
                break
        answer.append(str(sb))
    answer.append("-1")
    print(" ".join(answer))