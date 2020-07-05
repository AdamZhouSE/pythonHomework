def nappear(A):
    M=max(A)
    integer=0
    if M<=0:
        integer=0
    else:
        integer=M+1
    return integer

A=[1,2,0]
print(nappear(A))