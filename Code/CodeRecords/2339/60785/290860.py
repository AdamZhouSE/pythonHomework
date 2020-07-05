t=int(input())
for te in range(t):
    n=int(input())
    nums=[int(i) for i in input().split()]
    count=0
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if i==j :
                continue
            if nums[i]>nums[j]:
                count+=1
    print(count)