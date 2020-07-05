def isDiffByOne(word1,word2):
    diffNum=0
    for i in range(len(word1)):
        if word1[i]!=word2[i]:
            diffNum+=1
    if diffNum==1:
        return True
    return False


def dfs(beginword,endword,tmp:list,wordlist,res:list,cur,idx):
    if beginword==endword:
        if not len(res):
            res.append(tmp[:idx])
        elif idx<len(res[0]):
            res.clear()
            res.append(tmp[:idx])
        elif idx==len(res[0]):
            res.append(tmp[:idx])
        return

    if cur==len(wordlist):
        return

    if wordlist[cur] not in tmp[:idx] and isDiffByOne(beginword,wordlist[cur]):
        tmp[idx]=wordlist[cur]
        dfs(wordlist[cur],endword,tmp,wordlist,res,0,idx+1)
    dfs(beginword,endword,tmp,wordlist,res,cur+1,idx)


def findSequence(beginword,endword,wordlist):
    res=[]
    tmp=[beginword for i in range(len(wordlist)+1)]
    dfs(beginword,endword,tmp,wordlist,res,0,1)
    return res


beginword=input()
endword=input()
wordlist=eval(input())
res=findSequence(beginword,endword,wordlist)
if not len(res):
    print('[]')
else:
    print('[')
    for x in res:
        print(x)
    print(']')