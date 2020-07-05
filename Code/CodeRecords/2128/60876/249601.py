nums=list(map(int,input().split(",")))
temp=[]
def f(n):
    sum=0
    for i in range(0,len(nums)):
       sum+=nums[(i+n)%len(nums)]*i
    return sum
for i in range(0,len(nums)):
    temp.append(f(i))
temp.sort()
print(temp[len(temp)-1])