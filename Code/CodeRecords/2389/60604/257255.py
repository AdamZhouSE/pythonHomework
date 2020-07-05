n=int(input())
for I in range(n):
    l=int(input())
    a=input().split()
    #print(a)
    for i in range(l//2):
        tmp=a[i*2]
        a[i*2]=a[i*2+1]
        a[i*2+1]=tmp
    for i in range(l-1):
        print(a[i],end=' ')
    print(a[-1])
    