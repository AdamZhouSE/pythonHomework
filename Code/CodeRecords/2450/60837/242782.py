def exist(nums,target):
    start=-1
    end=-1
    num=0
    for i in range(len(nums)):
        if nums[i]==target:
            if num==0:
                start=i
                end=i
                num+=1
            else:
                end=i
    res=[]
    res.append(start)
    res.append(end)
    return res

nums=list(map(int,input().split(',')))
target=int(input())
print(exist(nums,target))