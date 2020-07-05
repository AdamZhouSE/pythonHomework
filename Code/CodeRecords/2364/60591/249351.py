def isRe(nums):
    nums = list(str(nums))
    if(len(set(nums)) != len(nums)):
        return True
    else:
        return False

n = eval(input())
count = 0
for x in range(1,n+1):
    if(isRe(x)):
        count += 1
print(count)