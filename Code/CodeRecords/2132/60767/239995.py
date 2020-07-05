characters = list(input())
nums = [0,1,2,3,4,5,6,7,8,9]
nums[0] = characters.count("z")
nums[2] = characters.count("w")
nums[4] = characters.count("u")
nums[6] = characters.count("x")
nums[8] = characters.count("g")
nums[1] = characters.count("o")-nums[0]-nums[2]-nums[4]
nums[3] = characters.count("h")-nums[8]
nums[5] = characters.count("f")-nums[4]
nums[7] = characters.count("s")-nums[6]
nums[9] = characters.count("i")-nums[5]-nums[6]
res = []
for i in range(0,10):
    if(nums[i]>0):
        for x in range(0,nums[i]):
            res.append(str(i))
print("".join(res))