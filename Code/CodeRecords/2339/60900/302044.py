n = int(input())
num =[]
for i in range(0,n):
    a = int(input())
    nums=input().split(' ')
    for j in range(0,len(nums)):
        nums[j] = int(nums[j])
    num.append(nums)
result=[]
for i in range(0,n):
    count =0
    for j in range(0,len(num[i])-1):
        for m in range(j+1,len(num[i])):
            if num[i][m] < num[i][j]:
                count+=1
    result.append(count)
for i in range(0,len(result)-1):
    print(result[i],end=' ')
print(result[len(result)-1])