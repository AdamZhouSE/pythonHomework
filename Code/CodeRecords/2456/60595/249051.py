def Test():
    nums=eval(input())
    result=[]
    for k in range(0,len(nums)):
        temp=nums[k]
        if(k+1<len(nums)):
            maps=nums[k+1:len(nums)]
            result.append(countRight(temp,maps))
        else:
            result.append(0)
    print(result)

def countRight(temp,nums):
    count=0
    for m in range(0,len(nums)):
        if(nums[m]<temp):
            count=count+1
    return count

if __name__ == "__main__":
    Test()