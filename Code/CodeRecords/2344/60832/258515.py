All = int(input())

for i in range(0, All):
    length=int(input())
    ar=input().split()
    d=int(input())

    ans=ar[d:]+ar[0:d]

    for x in ans:
        print(x,end=' ')
    print()