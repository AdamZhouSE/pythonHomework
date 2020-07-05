def multi(m1,m2):
    x1=m1[0][0]
    x2=m2[0][0]
    y1=m1[0][1]
    y2=m2[0][1]
    z1=m1[1][1]
    z2=m2[1][1]
    new_x=x1*x2
    new_y=x1*y2+y1*z2
    new_z=z1*z2
    return [[new_x,new_y],[0,new_z]]

nums = input().split(" ")
H = int(nums[0])
W = int(nums[1])
K = int(nums[2])
ls = []
for i in range(H):
    this = []
    s = input()
    for j in range(W):
        this.append(s[j])
    ls.append(this)
X = 0
for i in range(H):
    for j in range(W):
        if ls[i][j]=="#":
            X=X+1
W_connected = False  # 看左右是否连通
H_connected = False  # 看上下是否连通
for i in range(H):
    if ls[i][0] == "#" and ls[i][W - 1] == "#":
        W_connected = True
        break
for j in range(W):
    if ls[0][W-1] == "#" and ls[H - 1][W-1] == "#":
        H_connected = True
        break
if (H_connected and W_connected) or K==1:
    print(1)
elif not H_connected and not W_connected:
    print(pow(X, K - 1))
else:
    if W_connected and not H_connected:
        Z=0#左右连通的行数
        for i in range(H):
            if ls[i][0] == "#" and ls[i][W - 1] == "#":
                Z=Z+1
        Y=0#这行的下一个也是#的#数
        for i in range(H):
            for j in range(W-1):
                if ls[i][j]=="#" and ls[i][j+1]=="#":
                    Y=Y+1
    if H_connected and not W_connected:
        Z=0#上下联通的列数
        for j in range(W):
            if ls[0][W-1] == "#" and ls[H - 1][W-1] == "#":
                Z=Z+1
        Y=0#这列的下一个也是#的#数
        for j in range(W):
            for i in range(H-1):
                if ls[i][j]=="#" and ls[i][j+1]=="#":
                    Y=Y+1
    if K==2:
        print(X-Y)
    else:
        M=[[X,Y],[0,Z]]
        matrix=[]
        b=bin(K-2)[2:]
        i=len(b)-1
        this=[[X,Y],[0,Z]]
        while i>=0:
            if b[i]=="1":
                matrix.append(this)
            if i==0:
                break
            this=multi(this,this)
            i=i-1
        for i in range(len(matrix)):
            M=multi(M,matrix[i])
        print(M[0][0]-M[0][1])








