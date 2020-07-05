x=(int(input()))
y=(int(input()))
if(x>y):
    print(x-y)
else:
    count=0
    while y!=x:
        if y<x:
            count+=x-y
            break
        else:
            if(y%2==1):
                y+=1
                y=y/2
                count+=2
            else:
                y/=2
                count+=1
    print(int(count))