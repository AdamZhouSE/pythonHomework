sizes=list(map(int,input().split(' ')))
nums=list(map(int,input().split(' ')))
size=sizes[0]
t=sizes[1]
k=sizes[2]
i=0
j=0
res=0
while i<size:
    if(i-j==k):
        res=res+1
        j=j+1
    else:
        if(nums[i]>t):
            j=i+1
        i=i+1
if(i-j==k):
    res=res+1
print(res)