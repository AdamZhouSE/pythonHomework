def Test():
    nums=eval(input())
    nums=sorted(nums)
    print(find(nums))
def find(nums):
    try:
        if(nums.count(1)==0):
            return 1
        this=0
        for i in range(0,len(nums)):
            if(nums[i]>0):
                this=nums[i]
            if(nums[i+1]-this>1):
                return this+1
        return nums[-1]+1
    except:
        return nums[-1] + 1
if __name__ == "__main__":
    Test()