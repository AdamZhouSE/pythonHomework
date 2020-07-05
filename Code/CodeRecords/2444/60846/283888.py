import re
def func(nums,k,t):
    for i in range(len(nums)-k):
        if abs(nums[i]-nums[i+k])==t: return True
    return False
p=re.match(r'nums = (\S+), k = (\d), t = (\d)',input())
q=re.match(r'nums = (.+), k = (\d), t = (\d)',"nums = [1,2,3,1], k = 3, t = 0")
if func(eval(p.group(1)),int(p.group(2)),int(p.group(3))): print("true")
else: print("false")