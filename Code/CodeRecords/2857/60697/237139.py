size=int(input())
nums=list(map(int,input().split(' ')))
a=min(nums)
res=0
flag=False
tmp=[]
b=int(a**0.5)
for i in range(1,b+1):
    if(a%i==0):
        tmp.append(i)
        if(i!=int(a/i)):
            tmp.append(int(a/i))

for i in tmp:
    flag=True
    for j in nums:
        if(j%i!=0):
            flag=False
            break
    if(flag):
        res=res+1
print(res)
# 6
# 6 90 12 18 30 18