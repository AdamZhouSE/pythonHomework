s = int(input())
nums = input().split(",")
nums = list(map(int,nums))
shortestNums=nums
nowNums=[]
for i in nums:
    nowNums.append(i)
    summary = 0
    for j in nowNums:
        summary = summary + j
    if summary < s:
        continue
    while summary-nowNums[0] >= s:
        summary = summary - nowNums[0]
        nowNums.pop(0)
    if(len(nowNums)<len(shortestNums)):
        shortestNums = nowNums
print(len(shortestNums))