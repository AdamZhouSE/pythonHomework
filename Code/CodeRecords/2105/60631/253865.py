a = input()
b = a.split(',')
A=int(b[0])
B=int(b[1])
C=int(b[2])
D=int(b[3])
E=int(b[4])
F=int(b[5])
G=int(b[6])
H=int(b[7])
out = 0
if C <= E or H <= B or G <= A or D <= F:
    out = (C-A)*(D-B)+(G-E)*(H-F)
else:
    out =  (C-A)*(D-B)+(G-E)*(H-F)-min(min(C-E, G-A), min(C-A, G-E))*min(min(H-B, D-F), min(D-B, H-F))
print(out)