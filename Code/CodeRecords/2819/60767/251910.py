import math
def numOfCabs(nums):
    set(nums)
    one = nums.count(1)
    two = nums.count(2)
    three = nums.count(3)
    four = nums.count(4)
    res = four+three+int(two/2)
    two = two%2
    one = max(0,one-three)
    if(2*two+one<=4 and 2*two+one>0):
        res += 1
    else:
        if(two==1):
            res +=1
            res += math.ceil((one-2*two)/4)
        else:
            res += math.ceil(one/4)
    return res

n = input()
temp = input().split(" ")
nums = []
for t in temp:
    nums.append(int(t))
res = numOfCabs(nums)
print(res)
