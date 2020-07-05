nums=list(map(int,input().split(',')))
i=0
while True:
    if i<len(nums)-1:
        if nums[i+1]>=nums[i]:
            i+=1
        else:
            print(nums[i+1])
            break
    else:
        print(nums[0])
        break