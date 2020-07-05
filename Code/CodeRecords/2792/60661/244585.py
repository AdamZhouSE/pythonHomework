n=int(input())
nums=input().split(' ')
nums=[int(x) for x in nums]
outs=[]
count=0
for i in range(n):
    if nums[i]==1 and i!=0:
        count+=1
        outs.append(str(nums[i-1]))
outs.append(str(nums[n-1]))
print(count+1)
print(' '.join(outs))