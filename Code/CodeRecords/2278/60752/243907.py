num=int(input())
for n in range(num):
    size=int(input())
    a=list(map(int,input().split(' ')))
    for i in range(size-1):
        a[i]=a[i]^a[i+1]
    print(' '.join(map(str,a)))