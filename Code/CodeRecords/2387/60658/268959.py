n,m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
for i in range(m):
    x,l,r=[int(x) for x in input().split()]
    if x==0:
        arr = arr[:l-1]+sorted(arr[l-1:r])+arr[r:]
    if x==1:
        arr = arr[:l-1]+sorted(arr[l-1:r],reverse=True)+arr[r:]
q = int(input())

print(arr[q-1])