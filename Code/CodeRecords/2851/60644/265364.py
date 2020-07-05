n=int(input())
arr=[]
for i in range(0,n):
    arr=arr+[input().split()]
min=0
for i in range(0,n):
    if int(arr[i][0])+int(arr[i][1])>min:
        min=int(arr[i][0])+int(arr[i][1])
print(min)
