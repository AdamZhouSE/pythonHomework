Nv=int(input())
ds=[int(x) for x in input().split()]

class TNode:
    def __init__(self,val,d):
        self.val=val
        self.d=d

f=[[]]
root=[[]]
for i in range(1,Nv+1):
    f.append([])
    root.append([])
    for j in range(Nv+1):
        root[i].append(0)
        if j==0: f[i].append(0)
        elif i==j: f[i].append(ds[i-1])
        else: f[i].append(-1)

def dp(f,i,j):
    global root
    if i==j:
        root[i][i]=i
        return
    if i+1==j:
        root[i][j]=i
        root[i][i]=i
        root[j][j]=j
        f[i][j]=f[i][i]+f[j][j]
        return
    maxScore = 0
    for k in range(i,j+1):
        if k==i:
            dp(f,k+1,j)
            score=f[k+1][j]+f[k][k]
        elif k==j:
            dp(f,i,k-1)
            score=f[i][k-1]+f[k][k]
        else:
            dp(f,i,k-1)
            dp(f,k+1,j)
            score=f[i][k-1]*f[k+1][j]+f[k][k]
        if score>maxScore:
            maxScore=score
            root[i][j]=k
            f[i][j]=maxScore

dp(f,1,Nv)
print(f[1][Nv])

def getPreorder(root,lo,hi):
    if lo>hi:return
    rootIdx=root[lo][hi]
    print(rootIdx,'',end='')
    getPreorder(root,lo,rootIdx-1)
    getPreorder(root,rootIdx+1,hi)

getPreorder(root,1,Nv)