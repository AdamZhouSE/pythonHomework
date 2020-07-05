nums=input()[1:-1].split(",")
k=0
maxRes=0
while k<len(nums)-1:
    j=k+1
    str1=nums[k][1:-1]
    while j<len(nums):
        str2=nums[j][1:-1]
        judge=True
        for i in str1:
            if i in str2:
                judge=False
                break
        if judge==True:
            maxRes=max(maxRes,len(str1)*len(str2))
        j+=1
    k+=1
print(maxRes)