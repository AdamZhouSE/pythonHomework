n,x=input().split(' ')
xx=int(x)
info=input().split(' ')
a=[]
for num in info:
    a.append(int(num))
a.sort()
count=0
for i in range(len(a)):
    count=count+a[i]*xx
    if xx>1:
        xx=xx-1
print(count)
    
    
    