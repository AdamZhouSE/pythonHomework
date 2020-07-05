nums = input().split(",")
nums = list(map(int,nums))
numD = 0
numL = 0
for i in range(1,len(nums)+1):
    if nums.count(i) == 2:
        numD=i
        if numL != 0:
            break
    if nums.count(i) == 0:
        numL=i
        if numD != 0:
            break
answer = [numD,numL]
print(answer)