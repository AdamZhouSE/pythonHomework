t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr2=[]
    for j in range(len(arr)-1):
        arr2.append(arr[j]^arr[j+1])
    last=arr2[len(arr2)-1]^arr[len(arr)-2]
    arr2.append(last)
    result=''
    for j in range(len(arr2)-1):
        result+=str(arr2[j])+' '
    result+=str(arr2[j+1])
    print(result,end ='\n')