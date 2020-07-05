firstLine=input()
n=int(firstLine)
secondLine=input().split()
nums=[]
for i in secondLine:
    nums.append(int(i))
x=1
temp=1
for i in range(1,n):
    if nums[i-1]<nums[i]:
        temp+=1
    else:
        temp=1
    if temp>x:
        x=temp
print(x)