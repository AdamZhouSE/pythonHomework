def sortandcount(nums,left,mid,right,temp,indexes,res):
    for i in range(left,right+1):
        temp[i]=indexes[i]
    
    l = left
    r= mid+1
    for i in range(left,right+1):
        if l>mid:
            indexes[i]=temp[r]
            r+=1
        elif r>right:
            indexes[i]=temp[l]
            l+=1
            res[indexes[i]]+=(right-mid)
        elif nums[temp[l]]<=nums[temp[r]]:
            indexes[i]=temp[l]
            l+=1
            res[indexes[i]]+=(r-mid-1)
        else:
            assert nums[temp[l]]>nums[temp[r]]
            indexes[i]=temp[r]
            r+=1



def helper(nums,left,right,temp,indexes,res):
    if left==right:
        return 
    mid = left + (right-left)//2

    helper(nums,left,mid,temp,indexes,res)
    helper(nums,mid+1,right,temp,indexes,res)

    if nums[indexes[mid]]<=nums[indexes[mid+1]]:
        return
    sortandcount(nums,left,mid,right,temp,indexes,res)


nums = eval(input())
size = len(nums)
if size==0:
    print([])
    exit()
if size == 1:
    print([0])
    exit()
t = [None for i in range(size)]
i = [i for i in range(size)]
r = [0 for i in range(size)]
helper(nums,0,size-1,t,i,r)
print(r)