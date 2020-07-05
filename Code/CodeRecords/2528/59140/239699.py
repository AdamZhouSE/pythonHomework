str = input()
str = str[1:len(str) - 1]
nums = str.split(",")
nums=(int(x) for x in nums) # 列表迭代器
nums=list(nums) # generator to list
nums.sort() # 无返回值
print(nums)