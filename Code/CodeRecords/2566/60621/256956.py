# a=eval(input())
# d=[]
# for i in range(a):
#     d.append([int(x) for x in input().split(",")])
# c=[[i for i in j] for j in d]
# b=[[i for i in j] for j in d]
# for j in range(1,len(d[0])):
#     c[0][j]=c[0][j-1]+d[0][j]
# for i in range(1,a):
#     c[i][0]=c[i-1][0]+d[i][0]
# for i in range(1,a):
#     for j in range(1,len(d[0])):
#         c[i][j]=max(c[i-1][j],c[i][j-1])+d[i][j]
# for j in range(1,len(d[0])):
#     b[0][j]=min(b[0][j-1],c[0][j])
# for i in range(1,a):
#     b[i][0]=min(b[i-1][0],c[i][0])
# for i in range(1,a):
#     for j in range(1,len(d[0])):
#         b[i][j]=min(max(b[i-1][j],b[i][j-1]),c[i][j])
#
# print(b)
# print(b[a-1][len(d[0])-1])

b=eval(input())
a=[]
for i in range(b):
    a.append([int(x) for x in input().split(",")])
mimumHp=-1000000000000
m,n=len(a),len(a[0])
def dp(x,y,nowHp,LeastHp):
    global mimumHp
    nowHp+=a[x][y]
    LeastHp=min(LeastHp,nowHp)
    if LeastHp<mimumHp:
        return
    if(x==m-1 and y==n-1):
        mimumHp=max(mimumHp,LeastHp)
        return
    if(x==m-1):
        dp(x,y+1,nowHp,LeastHp)
    elif y==n-1:
        dp(x+1,y,nowHp,LeastHp)
    else:
        dp(x+1,y,nowHp,LeastHp)
        dp(x,y+1,nowHp,LeastHp)
    return

dp(0,0,0,0)
if mimumHp>=0:
    print(1)
else:
    print(mimumHp*(-1)+1)