n=int(input())
nums=list(map(int,input().split(" ")))
maxLength=1
i=0
while i<len(nums) and len(nums)-i>maxLength:
    j=i+1
    temp=[]
    temp.append(nums[i])
    while j<len(nums):
        if nums[j]>temp[-1] and nums[j]<=2*temp[-1]:
            temp.append(nums[j])
        elif nums[j]==temp[-1]:
            j+=1
            continue
        else:
            break
        j+=1
    maxLength=max(maxLength,len(temp))
    i+=1
print(maxLength)