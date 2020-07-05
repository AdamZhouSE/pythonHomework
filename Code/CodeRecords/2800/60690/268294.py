s1=input().split(" ")
n=int(s1[0])
d=int(s1[1])
nums=input().split(" ")
for i in range(n):
    nums[i]=int(nums[i])

isOk=False
res=0
while isOk==False:
    isChange=False
    for i in range(n-1):
        if nums[i]>=nums[i+1]:
            nums[i+1]+=d
            res+=1
            isChange=True
    if isChange==False:
        isOk=True
print(res)