s=str(input()).split(',')
s=list(map(int,s))
A=s[0]
B=s[1]
C=s[2]
D=s[3]
E=s[4]
F=s[5]
G=s[6]
H=s[7]
totalSquar = (D-B)*(C-A) + (H-F)*(G-E)
if (H < B) | (F > D) | (G < A) | (C < E):
    print(totalSquar)
else:
    if H > D:
        y1 = D
    else:
        y1 = H

    if B < F:
        y2 = F
    else:
        y2 = B

    y = abs(y1 - y2)
    if E < A:
        x1 = A
    else:
        x1 = E

    if C < G:
        x2 = C
    else:
        x2 = G
    x = abs(x1-x2)
    print(totalSquar - x*y)
