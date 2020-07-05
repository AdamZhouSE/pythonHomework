n=eval(input())
arr=[]
for _ in range(n):
    arr+=list(map(int,input().strip().split(',')))
k=eval(input())
arr=sorted(arr)
print(arr[k-1])