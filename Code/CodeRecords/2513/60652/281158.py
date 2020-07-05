N=int(input())
arr=[]
for row in range(N):
    a=list(map(int,input().split(',')))
    for i in a:
        arr.append(i)
k=int(input())        
arr.sort()
print(arr[k-1])