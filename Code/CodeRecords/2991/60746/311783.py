A=list(input())
def backwards(N):
    n=len(N)
    new=[]
    for i in range(n-1,-1,-1):
        if N[i]!=' ':
            new.append(N[i])
    s=''.join(new)
    return s
print(backwards(A))