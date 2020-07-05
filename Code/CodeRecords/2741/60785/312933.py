def findLengthOfLCIS( nums):
    length = len(nums)
    max_length = 1
    temp = 1
    if not nums:
        return 0
    for i in range(1, length):
        if nums[i] > nums[i - 1]:
            temp += 1
        else:
            max_length = max(max_length, temp)
            temp = 1
    max_length = max(max_length, temp)
    return max_length
num=input("")
nums=[]
nums=[]
dick={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
for i in num:
    if i in"1234567890":
        nums.append(dick[i])
print(findLengthOfLCIS(nums))