rb=input()
a=list(map(int,input().split()))
count=0
pos=0
res=0
for i in range(len(a)-1):
    if(a[i]>a[i+1]):
        count+=1
        pos=len(a)-i-1
if(count>1):
    res=-1
elif(count==1 and a[-1]>a[0]):
    res=-1
else:
    res=pos
print(res)
    
        