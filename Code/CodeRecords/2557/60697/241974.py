t=int(input())
nums=[]
for  i in range(t):
    nums.append(input())
res=[]
for i in range(t):
    res=[]
    num=nums[i]
    res.append(num[0])
    for j in range(1,len(num)):
        if(num[j]!=res[len(res)-1]):
            res.append(num[j])
    print("".join(res))
