n = (int)(input())
str = input()
nums = str.split(" ")

List = list(set(nums))
    
count = 0
for i in range(0,n):
    if(nums[i]=="0"):
        count= count+1
        
result = len(List)-count
if result ==0:
    result =1
    
print(result)