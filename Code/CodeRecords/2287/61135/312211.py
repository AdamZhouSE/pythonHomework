T=int(input())
for a in range(0,T):
    n=int(input())
    nums=input().split(" ")
    nums=list(int(x) for x in nums)
    result=list()
    for i in range(0,n-1):
        sign=0
        for j in range(i+1,n):
            if(nums[j]>=nums[i]):
                result.append(nums[j])
                sign=1
                break
            else:
                continue
        if(sign==0):
            result.append(-1)
    result.append(-1)
    result=list(str(x) for x in result)
    result=" ".join(result)
    print(result)
