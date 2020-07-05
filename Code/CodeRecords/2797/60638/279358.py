n=int(input())
numbers=list(map(int,input().split(" ")))
if n==1 :
    if numbers[0]==0:
        print("UP")
    elif numbers[0]==15:
        print("DOWN")
    else:
        print(-1)
else:
    if numbers[n-1]-numbers[n-2]<0:
        if numbers[n-1]==0:
            print("UP")
        else:
            print("DOWN")
    else:
        if numbers[n-1]==15:
            print("DOWN")
        else:
            print("UP")