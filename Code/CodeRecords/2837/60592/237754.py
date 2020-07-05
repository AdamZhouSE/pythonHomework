nums = input().split(' ')
total = int(nums[0])
l = int(nums[1])
r = int(nums[2])
small = pow(2,l)-1+total-l
big = pow(2,r)-1+(total-r)*pow(2,r-1)
print(small,end=" ")
print(big)
