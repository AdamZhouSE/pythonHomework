nums = input()
nums_new = (nums[1:len(nums)-1]).split(',')
for i in range(0,len(nums_new),2):
    if nums_new[i]!=nums_new[i+1]:
        print(int(nums_new[i]))
        break