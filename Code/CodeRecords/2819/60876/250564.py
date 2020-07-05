length=int(input())
nums=list(map(int,input().split(" ")))
start=0
jud=False
while 3 in nums:
    if 1 in nums:
        nums.append(4)
        del nums[nums.index(1)]
        del nums[nums.index(3)]
    else:
        break
while 1 in nums:
    start=nums.index(1)
    jud=False
    for i in range(start+1,len(nums)):
        if nums[i]==1:
            nums.append(2)
            del nums[i]
            del nums[start]
            jud=True
            break
    if not jud:
        break
while 2 in nums:
    start=nums.index(2)
    jud=False
    for i in range(start+1,len(nums)):
        if nums[i]==2:
            nums.append(4)
            del nums[i]
            del nums[start]
            jud=True
            break
    if not jud:
        while 1 in nums:
            startt=nums.index(1)
            judg=False
            for j in range(startt+1,len(nums)):
                if nums[j]==1:
                    nums.append(4)
                    del nums[start]
                    del nums[j]
                    del nums[startt]
                    judg=True
                    break
            if not judg:
                del nums[startt]
                del nums[start]
                nums.append(3)
                break
        break
if len(nums)==34:
    print(nums)
print(len(nums))
