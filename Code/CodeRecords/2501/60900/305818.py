n = int(input())
name1=input().split(' ')
name2=input().split(' ')
nums=[]
for i in range(0,n):
    nums.append(name1.index(name2[i]))
count = 0
for i in range(0,n-1):
    for j in range(i+1,n):
        if nums[i]>nums[j]:
            count+=1
print(count)