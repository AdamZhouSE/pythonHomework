str1 = input().split()
n = int(str1[0])
x0 = int(str1[1])
y0 = int(str1[2])
A = []
for x in range(n):
    xiyi = input().split()
    deltax = int(xiyi[0]) - x0
    deltay = int(xiyi[1]) - y0
    if deltay == 0:
        k = "max"
    else:
        k = deltax / deltay
    if k not in A:
        A.append(k)
print(len(A))
