import sys

t=int(sys.stdin.readline())
for i in range(0,t):
    num=int(sys.stdin.readline())
    for i in range(num,-1,-1):
        if i&num==i:
            print(i,end=" ")
    print()   