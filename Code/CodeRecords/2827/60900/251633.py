n = input()
str=input()
num = []

nums=str.split(" ")

for i in range(0,len(nums)):
        num.append((int)(nums[i]))

for i in range(0,int(n)):
    for j in range(0,int(n)-i-1):
        if(num[j]>num[j+1]):
            temp = num[j]
            num[j]= num[j+1]
            num[j+1] = temp

for i in range(0,int(n)-1):
    print(num[i],end=' ')
    
print(num[int(n)-1])