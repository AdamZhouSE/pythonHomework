n,x=input().split(' ')
info=input().split(' ')
a=[]
for num in info:
    a.append(int(num))
a.sort()
count=0
for i in range(len(a)):
    count=count+a[i]*int(x)
    if int(x)>1:
        int(x)=int(x)-1
print(count)
    
    
    