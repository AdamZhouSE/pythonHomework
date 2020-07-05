def solve():
    beginWord=input()
    endWord=input()
    dict=input()[1:-1].replace('"','').split(',')
    res=255
    possible=[]
    def dfs(begin,path,dic,pathw):
        nonlocal res
        if isNear(begin,endWord):
            path+=1
            possible.append(pathw+[endWord])
            if path<res:
                res=path
            return
        for i in range(len(dic)):
            if isNear(begin,dic[i]):
                word=dic[i]
                newDic=dic[:i]+dic[i+1:]
                dfs(word,path+1,newDic,pathw+[word])

    def isNear(begin,end):
        hasdif=False
        for i in range(len(begin)):
            if begin[i]!=end[i]:
                if not hasdif:
                    hasdif=True
                else:
                    return False
        return True

    dfs(beginWord,1,dict,[beginWord])
    if res==255:
        res=0
    reslist=[]
    for i in range(len(possible)):
        if len(possible[i])==res:
            reslist.append(possible[i])

    print(reslist)

if  __name__ == '__main__' :
    solve()