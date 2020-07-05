nums=int(input())
for i in range(nums):
    [n,k]=list(map(int,input().split(" ")))
    arr=list(map(int,input().split(" ")))
    temp=[]
    used=[]
    for j in range(len(arr)):
        if not arr[j] in temp:
            temp.append(arr[j])
        else:
            used.append(arr[j])
            temp.remove(arr[j])
    if len(temp)<k or temp[k-1] in used:
        print(-1)
    else:
        print(temp[k-1])