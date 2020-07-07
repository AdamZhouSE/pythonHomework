def printnum(n):
    if n==1:
        print(n, end=' ')
        return 1
    printnum(n-1)
    print(n,end=" ")

tc=int(input(""))
for _ in range(tc):
    n= int(input())
    printnum(n)
    print()
