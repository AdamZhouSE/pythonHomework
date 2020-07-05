nums=int(input())
arr=list(map(int,input().split(" ")))
count=0
for i in range(1,nums-1):
    if (arr[i]-arr[i-1])*(arr[i]-arr[i+1])>0:
        count+=1
print(count)