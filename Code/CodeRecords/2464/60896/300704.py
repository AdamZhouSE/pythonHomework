def find(nums,s):
    sum1=0
    left=0
    right=-1
    minlen=len(nums)
    while (right < len(nums)):
        while (sum1 < s and right < len(nums)):
            right+=1
            if(right>=len(nums)):
               break
            sum1 += nums[right]
        if (sum1 >= s):              
            if ((right - left + 1) < minlen):
                minlen = right - left + 1
            sum1 -= nums[left]
            left+=1
    return minlen
        

        
c=eval(input())
temp=input().split(',')
b=map(eval,temp)
list1=list(b)
print(find(list1,c))
