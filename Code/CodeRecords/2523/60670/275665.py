mat=eval(input())
n=len(mat)
m=len(mat[0])
#up=m-1
#down=n-1
#x-y
uplist=[[]for i in range(0,m)]#没有==0
downlist=[[]for i in range(0,n)]#x-y=0 放在downlist里？
for i in range(0,n):
    for j in range(0,m):
        if i-j<0:
            uplist[j-i].append(mat[i][j])
        else:
            downlist[j-i].append(mat[i][j])
for i in range(1,m):
    uplist[i]=sorted(uplist[i])
    for j in range(0,len(uplist[i])):
        mat[j][j+i]=uplist[i][j]
print(downlist)
for i in range(0,n):
    downlist[i]=sorted(downlist[i])
    for j in range(0,len(downlist[i])):
        mat[j+i][j]=downlist[i][j]
print(mat)
