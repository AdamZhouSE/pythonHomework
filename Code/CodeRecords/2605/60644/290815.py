e=input().split()
N=int(e[0])
M=int(e[1])
a=input().split()
for i in range(0,N):
    a[i]=int(a[i])
b=[[0]]*N
for i in range(0,N):
    b[i]=[a[i]]
for i in range(0,M):
    s=input().split()
    if s[0]=='1':
        x=int(s[1])
        y=int(s[2])
        for j in range(0,N):
            if b[j].count(a[x-1])>0:
                m=j
                if b[j].count(a[y-1])==0:
                    b[j]=b[j]+[a[y-1]]
            if b[j].count(a[y-1])>0:
                n=j
                if b[j].count(a[x-1])==0:
                    b[j]=b[j]+[a[x-1]]
        if len(b[m])>len(b[n]):
            b[n]=b[m]
        else:
            b[m]=b[n]
    if s[0]=='2':
        x=int(s[1])
        for j in range(0,len(b)):
            if b[j].count(x)>0:
                m=j
                break
        n=min(b[m])
        for j in range(0,len(b)):
            if b[j]==b[m]:
                b[j].remove(n)
        print(n)
