def panduan(z)->bool:
    try:
        z = int(z)
        return isinstance(z, int)
    except ValueError:
        return False
n=(int)(input())
for index in range(0,n):
    k=(int)(input())
    A =input().split(" ")
    now = []
    temp=1
    for index in range(len(A)):
        temp*=((int)(A[index]))
    k1=(int)(input())
    print(temp%k1)