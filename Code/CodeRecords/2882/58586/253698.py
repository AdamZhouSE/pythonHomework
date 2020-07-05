nums=int(input())
arr=list(map(int,input().split(" ")))
if nums==1:
    print("YES")
else:
    peek=-1
    index=-1
    for i in range(0,nums-1):
        if arr[i]>=arr[i+1]:
            index=i
            break
    if index==-1:
        print("YES")
    else:
        flag=True
        peek=arr[index]
        for i in range(index,nums-1):
            if arr[i]<arr[i+1]:
                flag=False
                break
        if flag:
            print("YES")
        else:
            print("NO")
