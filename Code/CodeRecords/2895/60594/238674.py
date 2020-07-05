def panduan(z:int)->bool:
    try:
        z = int(z)
        return isinstance(z, int)
    except ValueError:
        return False

A =input().replace("[",",").replace("]",",").replace(" ",",").split(",")
now = []
for index in range(len(A)):
    if panduan(A[index]):
        now.append((int)(A[index]))
a=now[0]
b=now[1]
while a<b:
    b=b&(b-1)
print(b)
