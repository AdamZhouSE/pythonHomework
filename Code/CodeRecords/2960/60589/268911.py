mn=input().split(' ')
m=int(mn[0])
n=int(mn[1])
a=input()
b=input()
heads=[]
for i in range(n-m+1):
    sub=b[i:i+m]
    crspnd=[False]*m
    for j in range(m):
        if a[j]==sub[j] or a[j]=='*' or sub[j]=='*':
            crspnd[j]=True
    if False not in crspnd:
        heads.append(str(i+1))
print(len(heads))
print(' '.join(heads)+' ')
