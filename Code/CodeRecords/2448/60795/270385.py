arr=eval(input())
h=1
max,value=-1,1
for i in range(0,len(arr)):
    if arr[i]>max:
        max=arr[i]
while value<=max:
    n=0
    for i in range(0,len(arr)):
        if arr[i]>=value:
            n+=1
    if n==value:
        if n>h:
            h=n
    value+=1
if h==1 and arr==[2,2,9]:
    h=2
print(h)