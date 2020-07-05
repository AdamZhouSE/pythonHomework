list1=input()
nums=[]
for x in list1:
    if(x=='I'):
        nums.append(1)
    elif(x=='V'):
        nums.append(5)
    elif(x=='X'):
        nums.append(10)
    elif(x=='L'):
        nums.append(50)
    elif(x=='C'):
        nums.append(100)
    elif(x=='D'):
        nums.append(500)
    elif(x=='M'):
        nums.append(1000)

length=len(nums)
num=0
for i in range(length-1):
    if(nums[i]<nums[i+1]):
        num-=nums[i]
    else:
        num+=nums[i]
num+=nums[length-1]

print(num)