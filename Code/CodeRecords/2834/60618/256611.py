n,m=map(int,input().split())
s=[['']*m]*n
A,B,C,D,E=0,0,0,0,0
for i in range(0,n):
    s[i]=list(input())
grade=[int(n) for n in input().split()]
re=0
for i in range(0,m):
    for j in range(0,n):
        if s[j][i]=='A':
            A+=1
        elif s[j][i]=='B':
            B+=1
        elif s[j][i]=='C':
            C+=1
        elif s[j][i]=='D':
            D+=1
        elif s[j][i]=='E':
            E+=1
    re=max(A,B,C,D,E)*grade[i]+re
    A,B,C,D,E=0,0,0,0,0
print(re)
            