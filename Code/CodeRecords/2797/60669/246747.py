
n=int(input())
arr=list(map(int,input().split()))

if n==1:
    if arr[0]==0:
        print("UP")
    else:
        print(-1)
else:
    if ( arr[len(arr)-2] - arr[len(arr)-1] ) > 0:
        if arr[len(arr)-2]==1 and arr[len(arr)-1]==0:
            print("UP")
        else:
            print("DOWN")
    else:
        if arr[len(arr)-2]==14 and arr[len(arr)-1]==15:
            print("DOWN")
        else:
            print("UP")