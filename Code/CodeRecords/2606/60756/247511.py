nums=list(map(int,input()[1:-1].split(",")))
target=int(input())
def binarySearch(begin:int,end:int,nums:list,target:int)->int:
    if begin<end:
        if nums[(begin+end)//2]==target:
            return (begin+end)//2
        elif nums[(begin+end)//2]>target:
            return binarySearch(begin,(begin+end)//2,nums,target)
        else:
            return binarySearch((begin+end)//2+1,end,nums,target)
    else:
        return -1
print(binarySearch(0,len(nums)-1,nums,target))