num=eval(input())
nums=input().split()
for i in range(0,len(nums)):
    nums[i]=int(nums[i])
cnt=0
result=[]
for i in range(0,len(nums)):
    if nums[i]==1 and i!=0:
        cnt+=1
        result.append(nums[i-1])
result.append(nums[len(nums)-1])
print(cnt+1)
for i in range(0,len(result)):
    if i!=len(result)-1:
        print(result[i],end='')
        print(' ',end='')
    else:
        print(result[i],end='')
        print('')