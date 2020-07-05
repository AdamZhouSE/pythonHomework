n=eval(input())
arr=list(map(int,input().strip().split(' ')))
if (n==1)&(arr[0]!=0):
    print(-1)
elif arr[n-1]==0:
    print("UP")
elif arr[n-1]==15:
    print("DOWN")
elif arr[n-1]>arr[n-2]:
    print("UP")
else:
    print("DOWN")