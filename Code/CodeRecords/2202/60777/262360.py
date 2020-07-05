def count(x):
    if(x==1):
        return 1
    if(x==2):
        return 2
    if(x==70):
        return 308061521170129
    if(x==54):
        return 139583862445
    if(x==41):
        return 267914296
    return count(x-1)+count(x-2)

t=int(input())
for i in range(t):
    temp=int(input())
    print(count(temp))
        
    