i = input()
l= len(i)-1
nums = i.split(",")
le= len(nums)
max= 0
for i in range(0,le):
    for j in range(i,le):
        temp = 0
        for m in range(i,j+1):
            temp+=int(nums[m])
        if(temp>=max):
            max=temp
print(max)
        
