num=int(input())
def Nim(N):
    n=N%4
    if n==0:
        return False
    else:
        return True
print(Nim(num))