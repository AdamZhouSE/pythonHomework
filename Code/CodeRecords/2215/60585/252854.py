arr=list(map(int,input().strip().split(',')))
n=len(arr)
print(arr[0],end='/(')
for i in range(1,n):
    if i!=n-1:
        print(arr[i],end='/')
    else:
        print(arr[i],end=')')
print()