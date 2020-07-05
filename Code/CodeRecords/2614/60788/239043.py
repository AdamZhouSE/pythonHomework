from sys import stdin
num=int(stdin.readline().strip())
for i in range(0,num):
    length=int(stdin.readline().strip())
    A=[int(x) for x in stdin.readline().split()]
    B=[int(x) for x in stdin.readline().split()]
    C=[int(x) for x in stdin.readline().split()]
    D=[]
    for j in range(0,length):
        D.append(A[j]-B[j])
    s=0
    for j in D:
        s+=C.count(j)
    print(s)
