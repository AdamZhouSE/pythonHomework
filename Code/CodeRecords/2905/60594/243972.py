def two(n:int)->int:
    temp=1
    for index in range (0,n):
        temp*=2
    return temp
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
temp=0
for index in range(len(now)):
    temp+=two(len(now)-1-index)*now[index]
print(temp)