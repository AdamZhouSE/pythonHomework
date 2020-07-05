def search(nums,left,right,target):
    if(left==right):
        if(nums[left]==target):
            return left
        else:
            return -1
    else:
        mid=(left+right)//2
        if(nums[mid]<target):
            return search(nums,mid,right,target)
        elif(nums[mid]>target):
            return search(nums,left,mid,target)
        else:
            return mid
        
str=input()
target=eval(input())
nums=eval(str)
print(search(nums,0,len(nums),target))