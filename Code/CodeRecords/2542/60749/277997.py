str1=input()
str1=str1.strip("[")
str1=str1.strip("]")
nums=list(map(int,str1.split(", ")))
nums=sorted(nums)
def findlongest(nums):
    maxlen=1
    templen=1

    for i in range(1,len(nums)):
        if nums[i]-nums[i-1]==1:
            templen+=1
        else:
            maxlen=max(maxlen,templen)
    return maxlen
print(findlongest(nums))