total=int(input())
results=[]
for i in range(total):
    num=int(input())
    arr=input().split(' ')
    arr=list(map(int,arr))
    result=''
    for a in range(len(arr)):
        if a==len(arr)-1:
            result+='-1'+' '
        else:
            if arr[a]>arr[a+1]:
                result+=str(arr[a+1])+' '
            else:
                result+='-1'+' '
    results.append(result)
for str in results:
    print(str)