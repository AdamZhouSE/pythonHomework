s1=str(input())
d=s1.count("]")-1
s2=[]
for g in s1:
    if g!='[' and g!=']'and g!=',':
        s2.append(g)
new=[]
a=0
s=[]
for v in s2:
    new.append(int(v))
    a=a+1
    if a==len(s2)/d:
        s.append(new)
        a=0
        new=[]
m,n=len(s),len(s[0])
for j in range(n):
    i,l,pos=0,[],[]
    while i< m and j<n:
        l.append(s[i][j])
        pos.append([i,j])
        i+=1
        j+=1
    l.sort()
    for i,p in enumerate(pos):
        x,y = p
        s[x][y]=l[i]
for i in range(1,m):
    j, l, pos = 0, [], []
    while i < m and j < n:
        l.append(s[i][j])
        pos.append([i, j])
        i += 1
        j += 1
    l.sort()
    for i, p in enumerate(pos):
        x, y = p
        s[x][y] = l[i]
print(s)