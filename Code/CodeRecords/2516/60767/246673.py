def getMinStart(arrs,k):
    start = arrs[k][1]
    minStart = 1000000000
    res = -1
    for i in range(0,len(arrs)):
        if(arrs[i][0]>=start):
            if(arrs[i][0]<minStart):
                minStart = arrs[i][0]
                res = i
    return res

n = int(input())
nums = []
for i in range(0,n):
    temp = input().split(",")
    temp2 = []
    for x in temp:
        temp2.append(int(x))
    nums.append(temp2)
res = []
for i in range(0,len(nums)):
    res.append(getMinStart(nums,i))
print(res)

