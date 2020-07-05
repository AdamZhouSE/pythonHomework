nums=input()
nums=nums[1:len(nums)-1]
ls=[]
ls=nums.split(",")
result="["
#print(ls)
for i in range(1,len(ls)):
    for j in range(0,i):
        temp=ls[i]
        if temp<ls[j]:
            break      #j是ls[i]应该停留的位置
    if i!=j:
        a=i
        while a>j:
            ls[a]=ls[a-1]
            a=a-1    
        ls[j]=temp
    #print(ls)
for i in range(0,len(ls)-1):
    result=result+ls[i]+", "
result=result+ls[len(ls)-1]+"]"
print(result)
    
            
        
      
