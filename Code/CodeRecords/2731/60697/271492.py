t=int(input())
sizes=[]
nums=[]
for i in range(t):
    sizes.append(int(input()))
    nums.append(list(map(int,input().split(' '))))
res=0
for i in range(t):
    size=sizes[i]
    j=0
    num=nums[i]
    num.sort()
    while(j<size-1):
        if(num[j]==num[j+1]):
            res+=2
            j=j+2
        else:
            j=j+1
print(res)