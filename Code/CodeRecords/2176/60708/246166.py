
def getcut(Str,length):
    cut=[]
    for i in range(0,length):
        temp=Str[i:]
        cut.append(temp)
    return cut
def sorting(cut):
    rank=[]
    l=len(cut)
    No=[]
    cuttemp=[]
    for item in cut:
        cuttemp.append(item)
    for i in range(0,l):
        temp=min(cut)
        for i, j in enumerate(cut):
            if j==temp:
                for x,y in enumerate(cuttemp):
                    if y==temp:
                        rank.append(x+1)
                cut.pop(i)
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