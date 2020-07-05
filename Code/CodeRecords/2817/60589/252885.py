n=int(input())
f=list(map(int,input().split(' ')))
l=[]
for i in range(n):
    s=str(i+1)
    s+=str(f[i])
    j=f[i]-1
    s+=str(f[j])
    j=f[j]-1
    s+=str(f[j])
    l.append(s)
has=False
for s in l:
    if len(set(s))==3:
        if s[0]==s[3]:
            has=True
            print('YES')
            break
if not has:
    print('NO')