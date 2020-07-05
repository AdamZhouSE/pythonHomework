x=int(input())
y=int(input())
n=y
if y>x:
    time=0
    while y!=x:
        if y%2==0 and y>x:
            y=y/2
        else:
            y+=1
        time+=1
    print(time)
else:
    print(x-y)