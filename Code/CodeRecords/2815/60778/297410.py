rb=input()
nums=list(map(int,input().split()))
count=0
res=0
has_zero=False
for i in nums:
    if(i<0):
        count+=1
        res+=-1-i
    elif(i>0):
        res+=i-1
    else:
        has_zero=True
        res+=1
if(count%2==1 and not has_zero):
    res+=2
print(res)