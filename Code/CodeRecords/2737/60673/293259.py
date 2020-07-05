n=input()
nums=n[1:-1].split(",")
for i in range(len(nums)):
    nums[i]=int(nums[i])
m=max(nums)
res=[]
for i in range(m):
    res.append(0)
for i in range(len(nums)):
    res[nums[i]-1]+=1
p=[]

for i in range(m):
    if(res[i]>int(len(nums)/3)):
        p.append(i+1)

print("[",end="")
for i in range(len(p)-1):
    print(p[i],end=", ")
print(p[len(p)-1],end="]")
print()


