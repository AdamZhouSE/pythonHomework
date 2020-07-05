T=int(input())
for i in range(T):
    n=int(input())
    nums=input().split(" ")
    for j in range(n):
        nums[j]=int(nums[j])
    result=[]
    for j in range(n-1):
        if nums[j]>nums[j+1]:
            result.append(nums[j+1])
        else:
            result.append(-1)
    result.append(-1)
    print(" ".join(str(i) for i in result)+" ")
