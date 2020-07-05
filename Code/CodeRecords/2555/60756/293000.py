n=int(input())
arr=list(map(int,input().split()))
thair=0
for i in range(n):
    for j in range(i+1,n):
        if arr[j]>arr[i]:
            for k in range(j+1,n):
                if arr[k]>arr[j]:
                    thair+=1
print(thair,end="")