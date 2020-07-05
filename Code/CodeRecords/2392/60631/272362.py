t=int(input())
for ti in range(t):
    si=input().split(' ')
    n=int(si[0])
    p=int(si[1])
    s=input().split(' ')
    ou=0
    for i in range(n):
        for j in range(i+1,n):
            if int(s[i])*int(s[j])==p:
                ou=1
    if ou==0:
        print('No')
    else:
        print('Yes')