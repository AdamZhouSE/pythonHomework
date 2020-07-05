def ifistree(this):
    #判断this是否是一棵树（即是否连通)
    n=len(this)#下标的最大值
    for i in range(n-1):
        for j in range(i+1,n):
            if i!=j:
                #看i和j是否连通
                tong=False
                a=i
                k=0
                while k<len(this):
                    has=False
                    if this[k][0]==a:
                        a=this[k][1]
                        has=True
                    elif this[k][1]==a:
                        a=this[k][0]
                        has=True
                    if a==j and has:
                        tong=True
                        break
                    k=k+1
                if not tong:
                    return False
    return True

s=input()
s=","+s[1:len(s)-2]
s=s.replace(" ",'')
ls=s.split("]")
have=[]#每个点有连接关系的点
ls=[x[2:] for x in ls]
#print(ls)
for i in range(len(ls)):
    ls[i]=ls[i].split(",")
    ls[i]=[int(x) for x in ls[i]]
    for j in range(len(ls[i])):
        ls[i][j]=ls[i][j]-1
#print(ls)
result=[]
for i in range(len(ls)):
    this=ls[:i]+ls[i+1:]
    if ifistree(this):
        result.append(ls[i])
for i in range(len(result)):
    result[i]=[x+1 for x in ls[i]]
#print(result)
print(result[len(result)-1])




