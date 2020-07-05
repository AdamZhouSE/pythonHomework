def solve():
    source=input()
    length=len(source)
    src=list(source)
    res=''
    if getAll(0,length,'',src):
        res='true'
    else:
        res='false'
    print(res)

def getAll(already,rest,lastRes,src=[]):
    if rest==0:
        if lastRes[0]=='0':
            return False
        if isTwo(int(lastRes)):
            return True
        else:
            return False
    else:
        for i in range(already+1):
            res=lastRes[0:i]+src[already]+lastRes[i:already]
            if getAll(already+1,rest-1,res,src):
                return True
        return False



def isTwo(num):
    if num==0:
        return False
    elif num==1:
        return True
    else:
        if num%2==1:
            return False
        else:
            return isTwo(int(num/2))

if  __name__ == '__main__' :
    solve()