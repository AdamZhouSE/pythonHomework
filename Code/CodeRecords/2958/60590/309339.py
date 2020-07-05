def check(s,l,r,len):
    for i in range(l,r+1):
        if s[i]!=s[(i-l)%len+l]:
            return False
    return True

s=input();n=len(s);s=' '+s
f=[]
m=[]
for i in range(101):
    if i<=9:
        m.append(1)
    elif i<100:
        m.append(2)
    else:
        m.append(3)
for i in range(n+1):
    f.append([])
    for j in range(n+1):
        if i==j:f[i].append(1)
        else:f[i].append(99)
for l in range(2,n+1):
    for i in range(1,n+2-l):
        j=i+l-1
        for k in range(i,j):
            f[i][j] = min(f[i][j], f[i][k] + f[k + 1][j])
        for k in range(i,j):
            len=k-i+1
            if(l%len!=0):continue
            if check(s, i, j, len):
                f[i][j]=min(f[i][j],f[i][k]+2+m[int(l/len)])
print(f[1][n])