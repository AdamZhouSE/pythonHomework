A=list(input())
def back(N):
    n=len(N)
    new=[]
    for i in range(n-1,-1,-1):
        new.append(str(N[i]))
    s=''.join(new)
    print(s)
    return 0
back(A)