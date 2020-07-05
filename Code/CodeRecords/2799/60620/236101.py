n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    while(a[i]%2==0):
        a[i]=a[i]//2
    while(a[i]%3==0):
        a[i]=a[i]//3
print('Yes' if min(a)==max(a) else 'No')
