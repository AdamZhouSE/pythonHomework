
def getcut(Str,length):
    cut=[]
    for i in range(0,length):
        temp=Str[i:]
        cut.append(temp)
    return cut
def sorting(cut):
    strnumber=[]
    for i in range(0,len(cut)):
        tempstr=""
        for j in range(0,len(cut)):
            if(len(cut[i])>j):
                tempstr=tempstr+str((ord(cut[i][j])))
            else:
                tempstr=tempstr+"00"
        strnumber.append(int(tempstr))
    L=len(strnumber)
    rank=[]
    for i in range(0,L):
        for x in range(0,len(strnumber)):
            if strnumber[x]>=0:
                minno=x
                minnuber = strnumber[x]
                break
        for j in range(0,len(strnumber)):
            a=strnumber[j]
            if a<minnuber and not a==-1:
                minnuber=strnumber[j]
                minno=j
        rank.append(minno+1)
        strnumber[minno]=-1
    return rank
if __name__ == '__main__':
    Str=input()
    cut=getcut(Str,len(Str))#存放后缀
    rank=sorting(cut)
    for i in range(0,len(rank)):
        if i!=len(rank)-1:
            print(rank[i],end='')
            print(" ",end='')
        else:
            print(rank[i])