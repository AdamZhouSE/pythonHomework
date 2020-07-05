[n,k]=list(map(int,input().split(" ")))
arr=list(map(int,input().split(" ")))
dif=[]
for i in range(n-1):
    dif.append(arr[i+1]-arr[i])
dif.sort(reverse=True)
sum=0
for i in range(k-1,n-1):
    sum+=dif[i]
print(sum)