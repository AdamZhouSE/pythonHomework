s=input()[1:-1].split(",")
for i in range(len(s)): s[i]=int(s[i])
s.sort()
k=int(input())

nums=[]

for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        l=[]
        l.append(s[i])
        l.append(s[j])
        nums.append(l)

for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        a=nums[i][0]/nums[i][1]
        b=nums[j][0]/nums[j][1]
        if a>b:
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
print(nums[k-1])