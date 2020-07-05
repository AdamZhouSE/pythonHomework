n=int(input())
nums=[]
for i in range(n):
    x=int(input())
    nums.append(x)

nums.sort()
sum=0
for i in range(1,n):
    sum+=nums[i]
print(sum)