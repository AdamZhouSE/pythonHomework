import math
def isSuperPaline(nums):
    sq = int(math.sqrt(nums))
    numS = str(nums)
    for x in range(int(len(numS)/2)):
        if (numS[x] != numS[len(numS) - 1 - x]):
            return False
    sqS = str(sq)
    for x in range(int(len(sqS)/2)):
        if(sqS[x] != sqS[len(sqS) - 1 - x]):
            return False
    return True

start = eval(input())
end = eval(input())
start1 = math.sqrt(start)
end1 = math.sqrt(end)
if(start1 > int(start1)):
    start = int(start1) + 1
else:
    start = int(start1)
end = int(end1)
cnt = 0
for x in range(start,end+1):
    if(isSuperPaline(x*x)):
        cnt += 1
print(cnt)