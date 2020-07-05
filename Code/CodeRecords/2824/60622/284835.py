a=input().split()
t=int(a[1])
c=int(a[2])
arr=list(map(int,input().split()))
count=0
for i in range(len(arr)-c+1):
    isOK=True
    for j in range(c):
        if arr[i+j]>t:
            isOK=False
            break
    if isOK:
        count+=1
print(count)

