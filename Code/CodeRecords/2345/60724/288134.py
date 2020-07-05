T=int(input())
for t in range(T):
    N=int(input())
    nums=input().split(" ")
    for i in range(N):
        nums[i]=int(nums[i])
    lose=0
    repetition=0
    for i in range(N):
        if not i+1 in nums:
            lose=i+1
            break
    nums.sort()
    for i in range(N-1):
        if nums[i]==nums[i+1]:
            repetition=nums[i]
            break
    result=str(repetition)+" "+str(lose)
    print(result)