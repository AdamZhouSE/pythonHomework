import math
s = input().split(',')
nums=[]
for i in range(0,len(s)):
    nums.append(int(s[i]))

list =list(set(nums))
result =0
for i in range(0,len(list)):
    a =math.ceil((nums.count(list[i])/(list[i]+1)))
    b =list[i]+1
    c = a*b
    result+=c

print(result)