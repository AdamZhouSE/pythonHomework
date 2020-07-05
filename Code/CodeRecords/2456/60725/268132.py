arrayString=input()
nums=eval(arrayString)
n=len(nums)
s=[]
for i in range(n):
    for j in range(i,n):
        if nums[j]<nums[i]:
            s[i]+=1
        else:
            s[i]+=0
print(s)           
        
        
            