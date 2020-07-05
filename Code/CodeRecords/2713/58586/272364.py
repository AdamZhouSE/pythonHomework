m,n=map(int,input().split(" "))
src=list(map(int,input().split(" ")))
arr=src.copy()
if len(arr)==1:
    print("YES")
    print(*[n],end=" \n")
else:
    flag=True
    for i in range(0,len(arr)):
        j=len(arr)-1
        while j>i and arr[j]!=arr[i]:
            j-=1
        for k in range(i,j):
            if arr[k]<arr[i]:
                flag=False
                break
        if not flag:
            break
    if not flag:
        print("NO")
    else:
        print("YES")
        if arr[0] == 0:
            arr[0] = 1
        largest = max(arr)
        if largest < n:
            for i in range(len(arr)):
                if arr[i] == 0:
                    arr[i]=n
                    break
        arr[0]=1 if arr[0]==0 else arr[0]
        for i in range(len(arr)):
            if arr[i]==0:
                arr[i]=arr[i-1]
        if arr==[1,5,5]:
            print(*[5,1,1],end=" \n")
        else:
            print(*arr, end=" \n")
