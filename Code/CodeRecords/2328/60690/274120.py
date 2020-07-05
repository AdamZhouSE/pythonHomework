nums=input().split(",")
for i in range(len(nums)): nums[i]=int(nums[i])
if min(nums)>2: print("")
else:
    res=""
    nums.sort()
    if 2 in nums:
        res="2"
        nums.remove(2)
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<4:
                res+=str(nums[i])
                nums.pop(i)
                break
        for i in range(len(nums) - 1, -1, -1):
            if nums[i]<6:
                res+=":"+str(nums[i])
                nums.remove(nums[i])
                res+=str(nums[0])
                break
        if len(res)<5:print("")
        else:print(res)
    elif 1 in nums:
        res="1"
        nums.remove(1)
        nums.sort()
        res+=str(nums[-1])+":"
        nums.pop(-1)
        if nums[-1]<6: res+=str(nums[-1])+str(nums[0])
        elif nums[-1]>5 and nums[0]<6: res+=str(nums[0])+str(nums[-1])
        else:res=""
        print(res)
    else:
        nums.sort()
        res="0"+str(nums[-1])+":"
        nums.pop(0)
        nums.pop(-1)
        if nums[-1]<6: res+=str(nums[-1])+str(nums[0])
        elif nums[-1]>5 and nums[0]<6: res+=str(nums[0])+str(nums[-1])
        else:res=""
        print(res)