IMP = [-1, -1]
A=list(map(int,input().split(',')))
S = sum(A)
if S % 3: print(IMP)
else:
    T = S / 3
    if T == 0:
        print([0, len(A) - 1])
    else:
        breaks = []
        su = 0
        for i, x in enumerate(A):
            if x:
                su += x
                if su in {1, T + 1, 2 * T + 1}:
                    breaks.append(i)
                if su in {T, 2 * T, 3 * T}:
                    breaks.append(i)

        i1, j1, i2, j2, i3, j3 = breaks

        if not (A[i1:j1 + 1] == A[i2:j2 + 1] == A[i3:j3 + 1]):
            print([-1, -1])
        else:
            x = i2 - j1 - 1
            y = i3 - j2 - 1
            z = len(A) - j3 - 1

            if x < z or y < z: print(IMP)
            else:
                j1 += z
                j2 += z
                print([j1, j2 + 1])