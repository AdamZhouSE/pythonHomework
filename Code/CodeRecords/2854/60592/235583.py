nums = input().split(' ')
nums.sort()
leg = 0
for i in range(0,3):
    if nums[i] == nums[i+1] and nums[i]==nums[i+2] and nums[i]==nums[i+3]:
        leg = i
        break
if leg == 2  and nums[0]== nums[1]:
    print("Elephant")
elif leg == 1 or leg == 2:
    print("Bear")
elif leg == 0 and nums[4] ==nums[5]:
    print("Elephant")
else:
    print("Alien")
    print(nums)