n=int(input())
for i in range(n):
    a=int(input())
    b=[int(x) for x in input().split(" ")]
    b.sort()
    for i in range(0,len(b)):
        print(str(b[i])+" ",end='')
    print()