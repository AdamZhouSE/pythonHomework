def test():
    n=int(input())
    string=input()
    strs=[]
    for _ in range(0,n):
        strs.append(input())
    str_split=[]
    for i in range(1,len(string)+1):
        if getMatch(string,0,str_split,strs,i):
            print(i)
            return
    print(-1)

def getMatch(string,begin,str_split,strs,segNum):
    if segNum==0:
        if begin < len(string):
            tmp=str(str_split.pop())
            tmp=tmp+string[begin:]
            str_split.append(tmp)
        if isMatch(str_split,strs):
            return True
        else:
            return False
    else:
        for i in range(begin,len(string)+1-segNum):
            copy_str_split=list(str_split)
            copy_str_split.append(string[begin:i])
            if getMatch(string,i,copy_str_split,strs,segNum-1):
                return True
            copy_str_split.pop()
        return False


def isMatch(str_split,strs):
    for seg in str_split:
        if seg not in strs:
            return False
    return True

test()