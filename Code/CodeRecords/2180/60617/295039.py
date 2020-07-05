def find_subStr():
    strA=input()
    strB=input()
    subStrA={}
    subStrB={}
    res=0
    for i in range(0,len(strA)):
        for j in range(i+1,len(strA)+1):
            if subStrA.get(strA[i:j],False):
                subStrA[strA[i:j]]+=1
            else:
                subStrA[strA[i:j]]=1
    for i in range(0,len(strB)):
        for j in range(i+1,len(strB)+1):
            if subStrB.get(strB[i:j],False):
                subStrB[strB[i:j]]+=1
            else:
                subStrB[strB[i:j]]=1
    for key in subStrA.keys():
        temp=subStrB.get(key,-1)
        if temp!=-1:
            res+=subStrA[key]*temp
    print(res,end="")

if __name__=='__main__':
    find_subStr()

