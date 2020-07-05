nums = list(map(int,input().split(',')))
count1 = nums.count(1)
if count1 % 3 != 0:
    print([-1,-1])
else:
    part,i = count1/3,0
    while part!=0:
        if nums[i]==1:
            part-=1
        i+=1
    left = i-1
    part = count1/3
    while part!=0:
        if nums[i]==1:
            part-=1
        i+=1
    right = i
    part1 = ""
    for i in range(0,left+1):
        part1+=str(nums[i])
    part2 = ""
    for i in range(left+1,right):
        part2+=str(nums[i])
    part3 = ""
    for i in range(right+1,len(nums)):
        part3+=str(nums[i])
    if int(part1)==int(part2)==int(part3):
        print([left,right])
    else:
        print([-1,-1])