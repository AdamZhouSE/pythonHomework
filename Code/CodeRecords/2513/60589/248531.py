n=int(input())
arr=[]
for i in range(n):
    row=input().split(',')
    row=list(map(int,row))
    arr.extend(row)
arr.sort()
k=int(input())
print(arr[k-1])