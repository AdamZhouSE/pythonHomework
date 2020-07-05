n=eval(input())
arr=list(map(int,input().strip().split(' ')))
count=0
zero=0
res=0
for i in arr:
    if i<0:
        res+=-1-i
        count+=1
    elif i>0:
        res+=i-1
    else:
        zero+=1
if count%2==1:
    if zero!=0:
        res+=zero
    else:
        res+=2
else:
    res+=zero
print(res)