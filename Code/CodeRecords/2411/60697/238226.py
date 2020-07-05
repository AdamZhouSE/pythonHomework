nums=[]
size=int(input())
for i in range(size):
    nums.append(list(map(int,input().split(','))))
s="True"
if nums[0][0]!=nums[1][0] and nums[0][1]!=nums[1][1]:
    for i in range(size):
        if((nums[i][0]-nums[0][0])*(nums[1][1]-nums[0][1])!=(nums[1][0]-nums[0][0])*(nums[i][1]-nums[0][1])):
            s="False"
            break
elif nums[0][0]==nums[1][0]:
    for i in range(size):
        if(nums[i][0]!=nums[0][0]):
            s="False"
            break
else:
    for i in range(size):
        if(nums[i][1]!=nums[0][1]):
            s="False"
            break
print(s)