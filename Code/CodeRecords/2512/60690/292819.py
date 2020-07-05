str=input().split(" ")
n=int(str[0])
p=int(str[1])
nums=input().split(" ")
for i in range(len(nums)):nums[i]=int(nums[i])
m=int(input())
res=[]
step=[]
for i in range(m):
    str=input().split(" ")
    step.append(str)
    if str[0]=="1":
        t=int(str[1])
        g=int(str[2])
        c=int(str[3])
        for j in range(t-1,g): nums[j]*=c
    elif str[0]=="2":
        t = int(str[1])
        g = int(str[2])
        c = int(str[3])
        for j in range(t-1,g):nums[j] +=c
    else:
        t = int(str[1])
        g = int(str[2])
        sum=0
        for j in range(t-1,g):sum+=nums[j]
        res.append(sum%p)
for e in res:print(e)

