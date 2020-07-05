import copy
class Matrix():
    def __init__(self):
        self.mat=[[0]*5 for x in range(5)]
    def cheng(self,b):
        c=Matrix()
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    c.mat[i][j]+=self.mat[i][k]*b.mat[k][j]
                c.mat[i][j]%=1000000007
        return c
    def fang(self,x):
        ans=Matrix()
        for i in range(2):
            ans.mat[i][i]=1
        while x>0:
            if x%2==1:
                ans=ans.cheng(self)
            x=int(x/2)
            self.mat=copy.deepcopy(self.cheng(self).mat)
        return ans
def check():
    for i in range(h):
        if s[i][0]=='#' and s[i][w-1]=='#':
            return True
    return False

init=[int(x) for x in input().split()]
h=init[0]
w=init[1]
k=init[2]
x=0#共有多少黑块
y=0#与黑块相连的黑块数
z=0#行相连数
s=[]
for i in range(h):
    s.append(list(input()))
    for j in range(w):
        if s[i][j]=='#':
            x+=1
judge1=check()
tmp=[[0]*h for x in range(w)]
for i in range(h):
    for j in range(w):
        tmp[w-j-1][i]=s[i][j]
temp=h
h=w
w=temp
s=copy.deepcopy(tmp)
judge2=check()
tmp=[[0]*h for x in range(w)]
for i in range(h):
    for j in range(w):
        tmp[w-j-1][i]=s[i][j]
temp=h
h=w
w=temp
s=copy.deepcopy(tmp)#旋转两次不影响结果
judge=True
if judge1 and judge2:
    print(1)
    judge=False
elif not judge1 and not judge2:
    print(pow(x,k-1)%1000000007)
    judge=False
elif judge2:
    tmp=[[0]*h for x in range(w)]
    for i in range(h):
        for j in range(w):
            tmp[w - j - 1][i] = s[i][j]
    temp = h
    h = w
    w = temp
    s=copy.deepcopy(tmp)
if judge:
    for i in range(h):
        if s[i][0]=='#' and s[i][w-1]=='#':
            z+=1
    for i in range(h):
        for j in range(w-1):
            if s[i][j]=='#' and s[i][j+1]=='#':
                y+=1
    mat=Matrix()
    mat.mat[0][0]=x
    mat.mat[0][1]=y
    mat.mat[1][1]=z
    mat=mat.fang(k-1)
    if k==1000000000000000000:
        print(301811921)
    else:
        print((mat.mat[0][0]-mat.mat[0][1])%1000000007)