num=int(input())
def power4(A):
    t=1
    for i in range(10000):
        k=A%4
        if k==0:
            A=A/4
            pass
        elif A==1:
            break
        elif k!=0:
            t=0
            break
    if t==1:
        return True
    elif t==0:
        return False
print(power4(num))