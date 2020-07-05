list0 = input().split(",")
str0 = ''.join(list0)
a = list(map(int,str0.split()))
A = a[0]
B = a[1]
C = a[2]
D = a[3]
E = a[4]
F = a[5]
G = a[6]
H = a[7]
if min(C, G) - max(A, E) < 0 or min(D, H) - max(B, F) < 0:
            S_overlap = 0
else:
    S_overlap = (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))
S_first_square = (D - B) * (C - A)
S_second_square = (H - F) * (G - E)
print(S_second_square + S_first_square - S_overlap)
