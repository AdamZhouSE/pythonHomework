nums=[int(x)for x in input().split(',')]
height = nums[7]-nums[1]
length = nums[2]-nums[4]
h1=abs(nums[3]-nums[1])
l1=abs(nums[2]-nums[0])
h2=abs(nums[7]-nums[5])
l2=abs(nums[6]-nums[4])
print(h1*l1+h2*l2-height*length)