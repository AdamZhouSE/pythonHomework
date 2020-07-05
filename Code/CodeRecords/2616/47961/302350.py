a=int(input())
for i in range (0,a):
    b=[int(i) for i in input().split()]
    k=(b[1]*(b[1]+1))/2
    if k<=b[0]:
        print(1)
    else:
        print(0)