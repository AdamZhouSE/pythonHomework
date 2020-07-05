def area(A,B,C,D,E,F,G,H):
    if min(C, G) - max(A, E) < 0 or min(D, H) - max(B, F) < 0:
        S_overlap = 0
    else:
        S_overlap = (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))
    S_first_square = (D - B) * (C - A)
    S_second_square = (H - F) * (G - E)
    return S_second_square + S_first_square - S_overlap
A,B,C,D,E,F,G,H=map(int,input().split(','))
print(area(A,B,C,D,E,F,G,H))