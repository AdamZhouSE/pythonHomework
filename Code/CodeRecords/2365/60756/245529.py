n=int(input())
for i in range(n):
    m=int(input())
    a=input().split()
    a.sort(reverse=True)
    for i in range(m-1):
        if len(a[i])!=len(a[i+1]):
            if int(a[i+1]+a[i])>int(a[i]+a[i+1]):
                temp=a[i]
                a[i]=a[i+1]
                a[i+1]=temp
    print(''.join(a))