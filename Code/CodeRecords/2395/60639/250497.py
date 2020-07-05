t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    for i in range(len(arr)-1):
        if arr[i+1]==arr[i]:
            arr[i]=arr[i]*2
            arr[i+1]=0
        else:
            continue
    num=arr.count(0)
    result=''
    for i in range(len(arr)):
        if arr[i]!=0:
            result+=str(arr[i])+' '
        else:
            continue
    for i in range(num):
        result+='0 '
    print(result.rstrip())