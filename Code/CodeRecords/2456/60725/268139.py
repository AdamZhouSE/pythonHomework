arrayString=input()
nums=eval(arrayString)
n=len(nums)
s=[]
count=0
for i in range(n):
    for j in range(i,n):
        if nums[j]<nums[i]:
            count+=1
        else:
            count=0
    s.append(count)
    count=0
print(s)        
        
            
            
        
           
           
        
        
            