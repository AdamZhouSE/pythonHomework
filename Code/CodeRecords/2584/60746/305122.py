def Nim(N):
    n=N%4
    if n==0:
        return False
    else:
        return True
N=4
print(Nim(N))