T=input()
A=list(input())
nn=len(A)
new=[]
for i in range(nn):
    if A[i].isdecimal():
        new.append(int(A[i]))
def arrangement(num,N):
    arrange=[]
    n=len(N)
    for i in range(0,n,2):
        