A=list(input())
B=list(input())
def connect(a,b):
    na=len(a)
    nb=len(b)
    new=[]
    for i in range(na):
        new.append(a[i])
    for i in range(nb):
        new.append(b[i])
    s=''.join(new)
    print(s)
    return 0
connect(A,B)