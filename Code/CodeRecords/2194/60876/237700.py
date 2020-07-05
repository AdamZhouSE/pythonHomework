import sys

n=int(sys.stdin.readline())
for i in range(0,n):
    m,n=map(int,sys.stdin.readline().split())
    temp=[]
    if m==1:
        m=2
    for j in range(m,n+1):
        jud=True
        for k in range(2,j):
            if j%k==0:
                jud=False
        if jud:
            temp.append(j)
    for j in range(0,len(temp)):
        if j!=len(temp)-1:
            print(temp[j],end=" ")
        else:
            print(temp[j])