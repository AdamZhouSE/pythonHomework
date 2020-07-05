m=int(input())
mat=[]
for i in range(m):
    li=list(map(int,input().split(',')))
    mat.append(li)
thr=int(input())
c=0
n=len(mat[0])
maxc=min(m,n)
for i in range(1,maxc+1):
    for j in range(m-i+1):
        for k in range(n-i+1):
            sign=0
            tmp=mat[j][k]
            for a in range(i):
                for b in range(i):
                    if mat[j+a][k+b]!=tmp:
                        sign=1
            if sign==0:
                t=tmp*i*i
                if t<=thr:
                    if i>c:
                        c=i

if c==1:
    print('2')
else:
    print(c)
    