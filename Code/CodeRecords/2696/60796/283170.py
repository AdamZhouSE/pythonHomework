def build(before,beforei,j):
    if j==N:
        result.append(before)
        return
    if j>0:
        beforen=before[j-1]#上一个数字
    else:
        return
    can=False
    for i in range(3):
        nown=ls[i][j]
        if i==0:
            if nown>=beforen:
                can=True
                build(before+[nown],0,j+1)
        elif i==1:
            if nown<=beforen:
                can=True
                build(before+[nown],1,j+1)
        elif i==2:
            if beforei==2 and nown>=beforen:
                can=True
                build(before+[nown],2,j+1)
            elif beforei==3 and nown<=beforen:
                can=True
                build(before+[nown],3,j+1)
            elif beforei!=2 and beforei!=3:
                can=True
                build(before+[nown],2,j+1)
                build(before+[nown],3,j+1)
        if length():
            return
    if not can:
        build(before,beforei,j+1)

    return


def length():
    for i in range(len(result)):
        if len(result[i])==N:
            return True
    return False

N=int(input())
ls=[]
for i in range(3):
    this=input().split(" ")
    this[i]=[int(x) for x in this[i]]
    ls.append(this)
result=[]
for i in range(3):
    this_before=[ls[i][0]]
    this_beforei=i
    build(this_before,this_beforei,1)
    if i==2:
        build(this_before,3,1)
    length()
    if length():
        break


m=0
for i in range(len(result)):
    if len(result[i])>m:
        m=len(result[i])
print(m)
