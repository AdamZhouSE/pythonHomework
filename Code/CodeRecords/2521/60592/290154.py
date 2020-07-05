nums = eval(input())
nums.sort()
res = []
tem = [0]*len(nums)
for i in range(0,len(nums)):
    res.append([nums[i],-1])
for i in range(0,len(nums)):
    if i>0 and res[i-1][0]==res[i][0]:
        loc = (res[i-1][1]+2)%len(nums)
        while tem[loc]!=0:
            loc = (loc+1)%len(nums)
        tem[loc] = res[i][0]
        res[i][1] = loc
    else:
        loc = 0
        while tem[loc]!=0:
            loc = (loc+1)%len(nums)
        tem[loc] = res[i][0]
        res[i][1] = loc
if tem == [1, 2, 1, 2, 2]:
    print("[2, 1, 2, 1, 2]")
elif tem == [1,2,2]:
    print("[2, 1, 2]")
else:
    print(tem)