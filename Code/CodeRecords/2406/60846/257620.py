n=int(input())
nums=[]
for i in range(n):
    nums.append(int(input()))

def getReverseNum(nums):
    cnt=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]: cnt+=1
    return cnt

def swap(nums,idx1,idx2):
    ret=[]
    for i in range(len(nums)):
        if i==idx1: ret.append(nums[idx2])
        elif i==idx2: ret.append(nums[idx1])
        else: ret.append(nums[i])
    return ret

reversePairsIdx=[]
for i in range(n):
    for j in range(i+1,n):
        if nums[i]>nums[j]: reversePairsIdx.append([i,j])
minTime=100000
for idx1,idx2 in reversePairsIdx:
    tmpNums=swap(nums,idx1,idx2)
    tmpTime=getReverseNum(tmpNums)
    if tmpTime<minTime: minTime=tmpTime
print(minTime)