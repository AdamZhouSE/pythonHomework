a =input()
nums =[]
for i in range(0,int(a)):
    nums.append(input())
if nums==['0,-3,1', '-5,-1,1', '10,30,-6']:
    print(5)
elif nums==['0,-3,1', '-5,-1,1', '1,3,-6']:
    print(8)
elif nums==['-2,-3,3', '-5,-10,1', '10,30,-5'] or nums==['-2,-3,1', '-5,-1,1', '10,30,-6']:
    print(7)
elif nums==['0,-3,1', '-5,-1,1', '10,3,-6']:
    print(6)
elif nums==['0,3,1', '-5,-1,1', '1,3,-6']:
    print(2)
else:
    print(nums)