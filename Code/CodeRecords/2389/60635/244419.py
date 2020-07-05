num = int(input())
for n in range(num):
    l = int(input())
    a = [int(x) for x in input().split()]
    for i in range(0,l-2,2):
        a[i],a[i+1]=a[i+1],a[i]
    print(*a)
    