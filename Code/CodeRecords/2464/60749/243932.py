s=int(input())
nums=input()
def search(s,nums):
    for x in nums:
        if x>=s:
            return 1
    sum_array=[]
    sum=0
    for x in range(0,len(nums)):
        sum+=nums[x]
        sum_array.append(sum)
    
    length=[]
    for i in range(0,len(nums)):
        for j in range(i,len(nums)):
            if sum_array[j]-sum_array[i]>=s:
                length.append(j-i)
    if len(length)==0:
        if sum_array[len(nums)-1]>=s:
            return len(nums)
        else:
            return 0
        
    else:
        return min( x for x in length)
print(search(s,nums))