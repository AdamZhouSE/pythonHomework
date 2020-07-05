length = int(input())
nums = []
for i in range(length):
    nums.append(list(map(int,input().split(','))))
nums.sort()    
x = nums[1][0] - nums[0][0]
y = nums[1][1] - nums[0][1]
for i in range(length-1):
    if x != nums[i+1][0] - nums[i][0]:
        print(False)
        quit()
    elif y != nums[i+1][1] - nums[i][1]:
        print(False)
        quit()
print(True)        
        