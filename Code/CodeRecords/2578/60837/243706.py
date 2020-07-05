def findNum(nums,threshold):
    i=1
    while sum(nums,i)>threshold:
        i+=1
    return i
    
def sum(nums,x):
    result=0
    for i in range(len(nums)):
        if nums[i]%x==0:
            result+=nums[i]/x
        else:
            result+=int(nums[i]/x)+1
    return result

nums=list(map(int,input().split(',')))
threshold=int(input())
print(findNum(nums,threshold))