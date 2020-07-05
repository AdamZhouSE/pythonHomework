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

flag=0
length=len(nums)
for i in range(length-2):
    if((nums[i]<nums[i+1])and(nums[i+1]>=nums[i+2])):
        flag=i
        break
number=0
for i in range(flag,length):
    number+=nums[i]
for i in range(flag-1):
    number-=nums[i]
print(number)