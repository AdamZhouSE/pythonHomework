def panduan(z)->bool:
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
max=1
n=1
for index in range(1,len(now)):
    if now[index]<=now[index-1]:
        n=1
    else:
        n+=1
        if max<n:
            max=n
print(max)