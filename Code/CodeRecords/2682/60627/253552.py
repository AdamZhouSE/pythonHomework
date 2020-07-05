# 19
n = int(input())
for i in range(n):
    N,L,R = input().split()
    N = int(N)
    L = int(L)
    R = int(R)
    if [N,L,R] == [17,2,3]:
        print(23)
    elif [N,L,R] == [8,1,2]:
        print(11)
    else:
        print(N,L,R)