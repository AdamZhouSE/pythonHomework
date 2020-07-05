def compareString(s,t):#比较s，t大小，长度不同则把短的用其最后一位补全
    slen = len(s)
    tlen = len(t)
    if(slen>tlen):
        t = t+(t[tlen-1]*(slen-tlen))
    elif(tlen>slen):
        s = s+(s[slen-1]*(tlen-slen))
    for i in range(0,len(s)):
        if(s[i]>t[i]):
            return True
        elif(s[i]<t[i]):
            return False
    return True

def insertSort(nums):
    for i in range (1,len(nums)):
        temp = nums[i]
        j = i
        while(j>0 and compareString(temp,nums[j-1])):
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = temp
    return nums

temp = input()[1:-1].split(",")
nums = []
for t in temp:
    nums.append(t)
nums = insertSort(nums)
res = ""
for i in range(0,len(nums)):
    res += nums[i]
print(res)