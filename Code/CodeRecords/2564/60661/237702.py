nums=input()[1:-1].split(',')
nums = [int(x) for x in nums]
k=int(input())
x=int(input())
if x>=nums[len(nums)-1]:
    print(nums[len(nums)-k:])
elif x<=nums[0]:
    print(nums[0:k])
else:
    res=[]
    pos=nums.index(x)
    res.append(nums[pos]);del nums[pos];pos-=1
    for i in range(k-1):
        if nums[pos]<=nums[pos+1]:
            res.append(nums[pos]);del nums[pos];pos -= 1
        else:
            pos+=1
            res.append(nums[pos]);del nums[pos];pos -= 1
    res.sort()
    print(res)