n=int(input())
a=[[0]*n]*n
b=[[0]*n]*n
for i in range(n):
    a[i]=list(input())
for i in range(0,n):
    for j in range(0,n-1):
        if a[i][j]=="o":
            b[i][j+1]+=1
        if a[i][j+1]=="o":
            b[i][j]+=1
        if a[j][i]=="o":
            b[j+1][i]+=1
        if a[j+1][i]=="o":
            b[j][i]+=1
num=1
for i in range(0,n):
    for j in range(0,n):
        if b[i][j]%2!=0:
            num=0
if num==1:
    print("YES")
else:
    print("NO")
    