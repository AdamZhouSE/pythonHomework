
num = input()
str = ""
nums = num.split(" ")
for i  in range (len(nums)-1):
    str = nums[i] +" "+ str
print(str,end='')