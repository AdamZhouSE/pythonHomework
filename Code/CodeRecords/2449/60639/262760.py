arr=list(map(int,input().split(',')))
n=int(input())
if n in arr:
    for i in range(len(arr)):
        if arr[i]==n:
            print(i)
            break
        else:
            continue
else:
    print(-1)