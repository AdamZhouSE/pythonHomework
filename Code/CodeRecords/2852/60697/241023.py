# 7
# 2 2 2 1 1 2 2
size=int(input())
nums=list(map(int,input().split(' ')))
a=0
b=0
maxsize=0
tmp=nums[0]
if(nums[0]==1):
    tmp=1
else:
    tmp=2
maxsize=0
for i in range(size):
    if(nums[i]==1):
        flag=1
    else:
        flag=2
    if (a > 0 and b > 0 and tmp == flag):
        maxsize=max(min(a,b),maxsize)
        if(tmp==1):
            tmp=2
            a=0
        else:
            tmp=1
            b=0
    if(nums[i]==1):
        a=a+1
    else:
        b=b+1
maxsize=max(min(a,b),maxsize)
print(maxsize*2)



