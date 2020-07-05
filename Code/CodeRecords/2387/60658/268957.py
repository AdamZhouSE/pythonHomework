n,m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
for i in range(m):
    x,l,r=[int(x) for x in input().split()]
    if x==0:
        arr = arr[:l]+sorted(arr[l:r+1])+arr[r+1:]
    if x==1:
        arr = arr[:l]+sorted(arr[l:r+1],reverse=True)+arr[r+1:]
q = int(input())
print(arr[q+1])