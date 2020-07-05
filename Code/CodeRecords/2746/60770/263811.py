def solve():
    beginWord=input()
    endWord=input()
    dict=input()[1:-1].replace('"','').split(',')
    res=255
    def dfs(begin,path,dic):
        nonlocal endWord
        nonlocal res
        if isNear(begin,endWord):
            path+=1
            if path<res:
                res=path
            return
        for i in range(len(dic)):
            if isNear(begin,dic[i]):
                word=dic[i]
                newDic=dic[:i]+dic[i+1:]
                dfs(word,path+1,newDic)

    def isNear(begin,end):
        hasdif=False
        for i in range(len(begin)):
            if begin[i]!=end[i]:
                if not hasdif:
                    hasdif=True
                else:
                    return False
        return True

    dfs(beginWord,1,dict)
    if res==255:
        res=0
    print(res)

if  __name__ == '__main__' :
    solve()