def isAppropriate(nums,length,average):
    if(sum(nums)==length*average):
        return True
    else:
        return False

def get_k_len_subset(nums,k):
    res = []
    temp = []
    length = len(nums)
    if(k==1):
        for i in nums:
            temp.append(i)
            res.append(temp)
            temp = []
        return res
    elif(k==length):
        res.append(nums)
        return res
    else:
        for i in range(0,length-k+1):
            for x in get_k_len_subset(nums[i+1:],k-1):
                temp = x
                temp.append(nums[i])
                res.append(temp)
                temp = []
    return res




nums = []
temp = input().split(",")
for i in temp:
    nums.append(int(i))
average = sum(nums)/len(nums)
res = False
for k in range(1,len(nums)):
    for x in get_k_len_subset(nums,k):
        if(isAppropriate(x,k,average)):
            res = True
print(res)