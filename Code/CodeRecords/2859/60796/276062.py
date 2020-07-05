n=int(input())
ls=[]
for i in range(n):
    ls.append(input())

diagonal=[]
for i in range(n):
    for j in range(n):
        if i==j or (i+j)==n-1:
            diagonal.append([i,j])
c1=True
c2=True

a=ls[0][1]
b=ls[0][0]
for i in range(n):
    for j in range(n):
        if not diagonal.__contains__([i,j]):
            if ls[i][j]!=a:
                c2=False
                break
        else:
            if ls[i][j]!=b:
                c1=False
                break
if c1 and c2:
    print("YES")
else:
    print("NO")