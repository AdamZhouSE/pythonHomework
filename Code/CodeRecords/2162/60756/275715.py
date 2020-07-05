X=float(input())
Y=int(input())
ans=1
if Y==0:
    print("1.00000")
else:
    if Y<0:
        Y=-Y
        X=1/X
    for i in range(Y):
        ans*=X
    print("{:.5f}".format(ans))