x=int(input())
y=int(input())
if x>y:
    print(x-y)
else:
    halfY=y
    time=0
    while int(halfY/2)>x:
        halfY=int(halfY/2)
        time+=1
    if halfY%2==0:
        time+=1+x-int(halfY/2)
    else:
        time+=1+2*x-halfY
    print(time)
