sum=int(input())
nums=list(map(int,input().split(" ")))
result=[]
total=1
temp=1
for i in range(0,sum-1):
    if nums[i]>=nums[i+1]:        
        result.append(temp)
        temp=1
        total+=1
    else:
        temp+=1
result.append(temp)
print(total)
length=len(result)
for i in range(0,length-1):
    print(result[i],end=" ")
print(result[length-1])