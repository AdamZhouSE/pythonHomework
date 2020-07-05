input()
num_list=[]
while(True):
    try:
        string=input()
        if string[-1]==",":
            string=string[:-1]
        num_list.append(eval(string))
    except:
        break
dx=[-1,0,1,0]
dy=[0,1,0,-1]
wid=len(num_list)
leng=len(num_list[0])
f=[]
res=0
for i in range(wid):
    f.append([0 for j in range(leng)])
def dp(x,y,m):
    if(f[x][y]!=0):
        return f[x][y]
    f[x][y]=1
    for i in range(4):
        a=x+dx[i]
        b=y+dy[i]
        if (a>=0 and a<wid and b<leng and b>=0 and m[a][b]>m[x][y]):
            f[x][y]=max(f[x][y],dp(a,b,m)+1)
    return f[x][y]
for j in range(wid):
    for k in range(leng):
        res=max(res,dp(j,k,num_list))
print(res)