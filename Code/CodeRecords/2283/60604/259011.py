n=int(input())
for I in range(n):
    l=input()
    a=input().split()
    a.sort()
    for i in range(len(a)-1):
        print(a[i],end=' ')
    print(a[-1])
    