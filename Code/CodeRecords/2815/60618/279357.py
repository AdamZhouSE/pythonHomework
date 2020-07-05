n= int(input())
a=[int(n) for n in input().split()]
negative=0
positive=0
zero=0
for i in range(0,n):
    if a[i]==0:
        zero+=1
    elif a[i]<0:
        negative+=1
    else:
        positive+=1
sum=0
if negative%2==0:
    for i in range(0,n):
        if a[i]==0:
            sum=sum+1
        elif a[i]>0:
            sum=sum+a[i]-1
        else:
            sum=sum+abs(a[i])-1
else:
    for i in range(0,n):
            
        if a[i]==0:
            sum=sum+1
        elif a[i]>0:
            sum=sum+a[i]-1
        else:
            sum=sum+abs(a[i])-1
        
    if zero==0:
        sum=sum+2
            
    
print(sum)