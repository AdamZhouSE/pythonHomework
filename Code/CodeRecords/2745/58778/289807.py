from collections import defaultdict
def findLadder(beginWord,endWord,wordList):
    wordList=set(wordList)
    res=[]
    #记录单词下一步能转换到的单词
    next_word_dict=defaultdict(list)
    #记录到beginWord的距离
    distance={}
    distance[beginWord]=0

    #找一个单词可以转换到的单词
    def next_word(word):
        ans=[]
        for i in range(len(word)):
            for j in range(97,123):
                #每个字母替换
                tmp=word[:i]+chr(j)+word[i+1:]
                if tmp!=word and tmp in wordList:
                    ans.append(tmp)
        return ans

    #使用bfs求到beginWord的距离
    def bfs():
        cur=[beginWord]
        step=0
        flag=False
        while cur:
            step+=1
            next_time=[]
            for word in cur:
                #将所有的nextWord加入字典中
                for nw in next_word(word):
                    next_word_dict[word].append(nw)
                    if nw==endWord:
                        flag==True
                    if nw not in distance:
                        distance[nw]=step
                        next_time.append(nw)
            if flag:
                break
            cur=next_time
    #遍历所有路径
    def dfs(tmp,step):
        if tmp[-1]==endWord:
            res.append(tmp)
            return
        for word in next_word_dict[tmp[-1]]:
            if distance[word]==step+1:
                dfs(tmp+[word],step+1)

    bfs()
    dfs([beginWord],0)
    return res
beginWord=input()
endWord=input()
wordList=eval(input())
print(findLadder(beginWord,endWord,wordList))