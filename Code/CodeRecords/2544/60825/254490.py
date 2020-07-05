def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)


N=int(input())
for i in range(N):
    s1=input()
    ls1=s1.split()
    ls1=list(map(int, ls1))

    A=[ls1[0], ls1[1]]
    B=[ls1[2], ls1[3]]

    s2=input()
    ls2=s2.split()
    ls2=list(map(int, ls2))

    C=[ls2[0], ls2[1]]
    D=[ls2[2], ls2[3]]

    if intersect(A,B,C,D):
        print(1)
    else:
        print(0)