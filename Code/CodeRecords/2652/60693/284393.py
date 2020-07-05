def findleftmin(gm:[[int]],n,i):
    money=sorted(gm[:i],key=lambda x:x[1])
    res=0
    for x in range(n//2):
        res+=money[x][1]
    return res

def findrightmin(gm:[[int]],n,i):
    money=sorted(gm[i+1:],key=lambda x:x[1])
    res=0
    for x in range(n//2):
        res+=money[x][1]
    return res


ncf=input().split()
n,c,f=int(ncf[0]),int(ncf[1]),int(ncf[2])
grade_money=list()
for _ in range(c):
    inp=list(map(int,input().split()))
    grade_money.append(inp)
grade_money=sorted(grade_money,key=lambda i:i[0])  # sorted by grade
res=-1
for i in range(c-n//2-1,n//2-1,-1):
    left=findleftmin(grade_money,n,i)
    right=findrightmin(grade_money,n,i)
    if left+right+grade_money[i][1]<=f:
        res=grade_money[i][0]
        break
print(res,end='')