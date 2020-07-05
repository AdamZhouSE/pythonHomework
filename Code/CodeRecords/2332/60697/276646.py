import sys
x=int(input())
target=int(input())
nums=[0 for i in range(32)]
len=0
while target>0:
    nums[len]=target%x
    target=target//x
    len+=1
lastReverse=sys.maxsize
ans=-1
i=len-1
while i>=0:
    if(i==0):
        m=2
    else:
        m=i
    forward=nums[i]*m
    reverse=(x-nums[i])*m+min(lastReverse-i-1,i+1)
    ans+=min(forward,reverse)
    if(forward>=reverse):
        lastReverse=0
    else:
        lastReverse=reverse-forward
    i-=1
print(ans)



