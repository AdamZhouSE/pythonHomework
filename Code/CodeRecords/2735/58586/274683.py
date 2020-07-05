n,m=map(int,input().strip().split(" "))
arr=list(map(int,input().strip().split(" ")))
for i in range(m):
    left,right,k=map(int,input().strip().split(" "))
    print(sorted(arr[left-1:right])[k-1])