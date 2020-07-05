nums=list(map(int,input().split(',')))
i=1
while True:
    if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
        print(i)
        break
    else:
        continue