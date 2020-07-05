from fractions import Fraction
A = list(int(n) for n in input().split(','))
N = len(A)
S = sum(A)
A = [z - Fraction(S, N) for z in A]
flag = False
if N == 1:
    flag = False
else:
    left = {A[0]}
    for i in range(1, int(N/2)):
        left = {z + A[i] for z in left} | left | {A[i]}
    if 0 in left:
        flag = True

    right = {A[-1]}
    for i in range(int(N/2), N-1):
        right = {z + A[i] for z in right} | right | {A[i]}
    if 0 in right:
        flag = True
    sleft = sum(A[i] for i in range(int(N/2)))
    sright = sum(A[i] for i in range(int(N/2), N))

    flag = any(-ha in right and (ha, -ha) != (sleft, sright) for ha in left)
print(flag)