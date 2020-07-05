n=int(input())
arr=list(map(int,input().split()))

arr.sort()
count=0;
for i in range(1,arr[0]+1):
    isX=True
    for num in arr:
        if num%i!=0:
            isX=False
            break
    if isX:
        count+=1
print(count)
