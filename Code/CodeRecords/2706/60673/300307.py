def isNotIn(e,nums):
    for i in range(len(nums)):
        for j in range(1,len(nums[i])):
            if(nums[i][j]==e):return False
    return True

def getIndex(e,nums):
    for i in range(len(nums)):
        for j in range(1,len(nums[i])):
            if(nums[i][j]==e):
                return i
    return -1

inp=input()
emails=inp[2:-2].split("], [")
for i in range(len(emails)):
    emails[i]=emails[i][1:-1].split("\", \"")
res=[]
for i in range(len(emails)):
    temp = []
    temp.append(emails[i][0])
    for j in range(1,len(emails[i])):
        if(isNotIn(emails[i][j],res)):
            temp.append(emails[i][j])
        else:
            for p in range(1,len(emails[i])):
                if(p!=j):
                    res[getIndex(emails[i][j],emails)].append(emails[i][p])
            break
    if(len(temp)!=1):
        res.append(temp)
print(res)

