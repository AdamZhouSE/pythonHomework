a=eval(input())
b=eval(input())
c=eval(input())
min=0
max=0
arr=sorted([a,b,c])
d1=arr[1]-arr[0]
d2=arr[2]-arr[1]
if d1>1:
    max=max+d1-1
    min=min+1
if d2>1:
    max=max+d2-1
    min=min+1
if d1==2 or d2==2:
    min=1
print("[",min,", ",max,"]",sep="")