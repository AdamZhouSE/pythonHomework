nums = input().replace(",","/")
string = nums[0:nums.index("/")+1]+"("+nums[nums.index("/")+1:]+")"
print(string)
