#07
from itertools import combinations
ori = input().replace("  "," ")
ori = ori.split(" ")
K = int(ori[0])
M = int(ori[1])
nums = [1]
while len(nums) <= 50:
    temp = nums[:]
    for item in nums:
        #print(item)
        if ( item * 2 +1 ) not in nums:
            temp.append(2*item+1)
        if ( item * 4 +5 ) not in nums:
            temp.append(4*item+5)
    nums = temp
    #print("temp: ",temp)
nums.sort()
s = ""
for i in range(0,K):
    s += str(nums[i])
print(s)
leftCount = len(s) - M
l = list(combinations(s,leftCount))
maxValue = 0
for item in l:
    s = ""
    for c in item:
        s += c
    if int(s) > maxValue:
        maxValue = int(s)
print(maxValue,end="")
