def solve(nums):
    nums=sorted(nums)
    a=nums[0]
    count=0
    list=[]
    for i in range(0,len(nums)):
        if(a==nums[i]):
            count+=1
            if(count>len(nums)/3):
                list.append(a)
        else:
            a=nums[i]
            count=1
            if(i==len(nums)-1):
                if(count>len(nums)/3):
                    list.append(a)
    return list
list=input().split(',')
list[0]=(list[0]).split('[')[1]
list[len(list) - 1]=list[len(list) - 1].split(']')[0]
list=[int(i) for i in list]
print(solve(list))
