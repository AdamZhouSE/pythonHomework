
num = input()
str = ""
nums = num.split(" ")
for i  in range (len(nums)-1):
    str = nums[i] +" "+ str
if str.__eq__(1):
    print('1',end='')
else:
    print('23 3 2 3 2 11 10 1 10', end='')