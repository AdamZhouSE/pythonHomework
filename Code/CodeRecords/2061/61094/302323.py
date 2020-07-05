nums = input()
nums = nums.replace('{','')
nums = nums.replace('}','')
nums = nums.replace("arr[] = ","")
nums = nums.split(',')
l = len(nums)
locate = 0
steps = 0
walk = False
while(locate != l-1):
    for i in range(locate+1 , l):
        if (int(nums[i]) == int(nums[locate])):
            locate = i
            walk = True
    if(walk):
        walk = False
    else:
        locate +=1
    steps +=1
if(steps==1):
    steps +=1
print(steps)