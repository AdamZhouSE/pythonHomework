from fractions import Fraction

A = [int(x) for x in input().split(',')]
N = len(A)
S = sum(A)
A = [z - Fraction(S, N) for z in A]

if N == 1:
    print(False)
else:
    left = {A[0]}
    for i in range(1, N//2):
        left = {z + A[i] for z in left} | left | {A[i]}
    if 0 in left:
        print(True)
    else:
        right = {A[-1]}
        for i in range(N//2, N-1):
            right = {z + A[i] for z in right} | right | {A[i]}
        if 0 in right:
            print(True)
        else:

            sleft = sum(A[i] for i in range(N//2))
            sright = sum(A[i] for i in range(N//2, N))
            print(any(-ha in right and (ha, -ha) != (sleft, sright) for ha in left))






