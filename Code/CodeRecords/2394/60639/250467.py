T=int(input())
for i in range(T):
    n=int(input())
    arr=list(map(int,input().split()))
    num=arr.count(0)
    result=''
    for i in range(n):
        if arr[i]!=0:
            result+=str(arr[i])+' '
        else:
            continue
    for i in range(num):
        result+='0 '
    print(result)