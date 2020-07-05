def Test():
    nums=eval(input())
    nums=sorted(nums)
    result=0
    i=0
    while(i<len(nums)):
        if(nums[i])<0:
            nums.remove(nums[i])
        else:
            i=i+1
    for i in range(0,len(nums)):
        if(i+1<len(nums)):
            if(abs(nums[i+1]-nums[i])>=2):
                result=(nums[i+1]+nums[i])//2
                break
    if(result==0):
        if(nums.count(1)==0):
            result=1
        else:
            result=nums[-1]+1
    print(result)
if __name__ == "__main__":
    Test()