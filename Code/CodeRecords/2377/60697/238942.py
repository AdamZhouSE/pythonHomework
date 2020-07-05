size=int(input())
nums=[]
for i in range(size):
    nums.append(list(map(int,input().split(','))))
s="True"
if(nums[0][0]==nums[1][0] and nums[0][1]==nums[1][1]) or (nums[0][0]==nums[2][0] and nums[0][1]==nums[2][1]) or (nums[1][0] == nums[2][0] and nums[1][1] == nums[2][1]):
    s="False"
if nums[0][0]!=nums[1][0] and nums[0][1]!=nums[1][1]:
    for i in range(2,size):
        if((nums[i][0]-nums[0][0])*(nums[1][1]-nums[0][1])==(nums[1][0]-nums[0][0])*(nums[i][1]-nums[0][1])):
            s="False"
            break
elif nums[0][0]==nums[1][0]:
    for i in range(2,size):
        if(nums[i][0]==nums[0][0]):
            s="False"
            break
else:
    for i in range(2,size):
        if(nums[i][1]==nums[0][1]):
            s="False"
            break
print(s)

