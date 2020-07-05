n,k=map(int,input().split(' '))
arr=list(map(int,input().split(' ')))
head=0
tail=n-1
for i in range(n):
    if(arr[i]>k):
        head=i
        break
if(i==n-1):
    print(n)
else:
    for i in range(n-1,-1,-1):
        if (arr[i] > k):
            tail = i
            break
    tail=(n+i)%n
    print(head+n-tail-1)

