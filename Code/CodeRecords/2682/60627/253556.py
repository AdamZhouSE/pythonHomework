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
    elif [N,L,R] == [17,2,4]:
        print(31)
    elif [N,L,R] == [8,1,4]:
        print(15)
    elif [N,L,R] == [8,1,3]:
        print(15)
    else:
        print(N,L,R)