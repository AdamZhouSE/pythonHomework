import copy
def trans():
    beginWord=input()
    endWord=input()
    wordList=list(eval(input()))
    res=[]
    length=2**16
    finalRes=[]
    if endWord not in wordList:
        print([])
        return
    else:
        wordList.insert(0,beginWord)
        tar=wordList.index(endWord)
    graph=[[-1 for i in range(0,len(wordList))] for i in range(0,len(wordList))]
    for i in range(0,len(wordList)):
        for j in range(0,len(wordList)):
            count=0
            if i!=j:
                a=wordList[i]
                b=wordList[j]
                for k in range(0,len(a)):
                    if count>1:
                        break
                    if a[k]!=b[k]:
                        count+=1
            if count<=1 and i!=j:
                graph[i][j]=1
                graph[j][i]=1
    for i in range(1,len(wordList)):
        temp=[wordList[0]]
        if graph[0][tar]==1:
            res.append(beginWord)
            res.append(endWord)
            print(res)
            return
        if graph[0][i]==1:
            temp.append(wordList[i])
            tmpGraph=copy.deepcopy(graph)
            for j in range(0,len(wordList)):
                tmpGraph[j][i]=-1
            tmpGraph[i][0]=-1
            dfs(tmpGraph,temp.copy(),res,wordList,i,tar)
    for sequence in res:
        length=min(length,len(sequence))
    for sequence in res:
        if len(sequence)==length:
            finalRes.append(sequence)
    print(finalRes)
def dfs(graph,temp,res,wordlist,start,tar):
    if graph[start][tar]==1:
        temp.append(wordlist[tar])
        res.append(temp)
        return
    else:
        for i in range(0,len(wordlist)):
            if graph[start][i]==1:
                temp.append(wordlist[i])
                tmpGraph=copy.deepcopy(graph)
                for j in range(0,len(wordlist)):
                    tmpGraph[j][i]=-1
                tmpGraph[i][start]=-1
                dfs(tmpGraph,temp.copy(),res,wordlist,i,tar)
                temp.pop()
        return
if __name__=='__main__':
    trans()