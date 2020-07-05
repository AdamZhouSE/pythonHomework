A=list(input())
def backwards(N):
    n=len(N)
    new=[]
    for i in range(n-1,-1,-1):
        new.append(str(N[i]))
    s=''.join(new)
    return s
print(backwards(A))