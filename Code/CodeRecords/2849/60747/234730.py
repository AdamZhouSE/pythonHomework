n=int(input())
arr=input().split(" ")
arr = list(map(int, arr))
arr.sort()
s=0
if n==1:
    print(arr[0])
else:
    for i in range(0,n):
        if int(arr[i])%int(arr[0])==0:
            continue
        else:
            print(-1)
            s=-1
            break
    if s!=-1:
        print(arr[0])