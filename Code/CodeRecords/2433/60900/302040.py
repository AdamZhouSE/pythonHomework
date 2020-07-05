str2 = input()
str2=str2.replace('[','')
str2=str2.replace(']','')
nums = str2.split(',')
for i in range(0,len(nums)):
        nums[i]=int(nums[i])

start=[]
end=[]
for i in range(0,len(nums)):
    if i%2 ==0:
        start.append(nums[i])
    else:
        end.append(nums[i])
result =[]
start.sort()
end.sort()
j = 0
for i in range(0,len(start)):
    if i==len(start)-1 or start[i+1]>end[i]:
        result.append([start[j],end[i]])
        j=i+1

print(result)