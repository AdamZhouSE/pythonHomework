n=int(input())
ls=[]
for i in range(n):
    m=input()
    l=[]
    for j in range(n):
        l.append(m[i])
    ls.append(l)
result=""
r=[]
for i in range(n):
    for j in range(n):#现在是ls[i][j]
        total=0
        if i>0:#有左
            if ls[i-1][j]=='o':
                total=total+1
        if i<n-1:#有右
            if ls[i+1][j]=='o':
                total=total+1
        if j<n-1:#有下
            if ls[i][j+1]=='o':
                total=total+1
        if j>0:#有上
            if ls[i][j-1]=='o':
                total=total+1
        if total%2==0:
            r.append(ls[i][j])
if len(r)==n*n:
    result="YES"
else:
    result="NO"
print(result)
        
        