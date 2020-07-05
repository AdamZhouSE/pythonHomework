arr=list(map(int,input().strip().split(',')))
target=eval(input())
n=len(arr)
isFound=False
for i in range(n):
    if arr[i]==target:
        isFound=True
        break
if isFound:
    print(i)
else:
    i=0
    while i<n:
        if target>arr[i]:
            i+=1
        else:
            break
    print(i)
    