T = int(input())
for a in range(0,T):
    N = int(input())
    A = input().split(' ')
    B = input().split(' ')
    A.sort()
    B.sort()
    if A==B:
        print(1)
    else:
        print(0)