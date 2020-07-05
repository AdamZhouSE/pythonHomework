def panduan(z)->bool:
    try:
        z = int(z)
        return isinstance(z, int)
    except ValueError:
        return False

A =input().replace("[",",").replace("]",",").split(",")
now = []
for index in range(len(A)):
    if panduan(A[index]):
        now.append((int)(A[index]))
B =input().replace("[",",").replace("]",",").split(",")
for index in range(len(B)):
    if panduan(B[index]):
        now.append((int)(B[index]))
now.sort()
print(now)