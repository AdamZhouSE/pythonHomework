n=int(input())
arr=list(map(int,input().split(" ")))
arr.sort()

output=0
if n!=2:
    x1=arr[1]-arr[0]
    x2=arr[-1]-arr[-2]
    if x2-x1>=0:
        output=arr[-2]-arr[0]
    else:
        output=arr[-1]-arr[1]
print(output)        